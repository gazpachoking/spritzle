#
# spritzle/resume_data.py
#
# Copyright (C) 2016 Andrew Resch <andrewresch@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.    If not, write to:
#   The Free Software Foundation, Inc.,
#   51 Franklin Street, Fifth Floor
#   Boston, MA    02110-1301, USA.
#

import asyncio
import binascii
import functools
import logging
from pathlib import Path

import libtorrent as lt

log = logging.getLogger('spritzle')


class ResumeData(object):
    def __init__(self, core):
        self.core = core
        self.loop = asyncio.get_event_loop()
        self.save_loop_task = None
        self.run = False

        # Store state of outstanding save resume data alerts
        self.resume_data_futures = {}

    async def start(self):
        log.debug('Resume data manager starting...')
        self.core.alert.register_handler(
            'save_resume_data_alert',
            self.on_save_resume_data_alert
        )
        self.core.alert.register_handler(
            'save_resume_data_failed_alert',
            self.on_save_resume_data_failed_alert
        )
        self.save_loop_task = asyncio.ensure_future(self.save_loop_coro())

    async def stop(self):
        log.debug("Resume data manager stopping...")
        if self.save_loop_task:
            self.save_loop_task.cancel()
            await self.save_loop_task
        log.debug("Resume data manager stopped.")

    async def save_loop_coro(self):
        try:
            while True:
                await asyncio.sleep(self.core.config['resume_data_save_frequency'])
                # Shield from cancellation while saving resume data
                await self.save()
        except asyncio.CancelledError:
            pass

    async def on_save_resume_data_alert(self, alert):
        info_hash = str(alert.handle.info_hash())
        p = Path(self.core.state_dir, alert.torrent_name + '.resume')
        r = lt.write_resume_data(alert.params)
        r.update(self.core.torrent_data[info_hash])
        p.write_bytes(lt.bencode(r))
        if info_hash in self.resume_data_futures:
            self.resume_data_futures.pop(info_hash).set_result(True)

    async def on_save_resume_data_failed_alert(self, alert):
        log.error(
            f'Error saving resume_data for torrent {alert.torrent_name} '
            f'error: {alert.error.message()}')
        info_hash = str(alert.handle.info_hash())
        if info_hash in self.resume_data_futures:
            # We don't really care if this fails right now, maybe in the future
            # we should raise an exception.
            self.resume_data_futures.pop(info_hash).set_result(True)

    async def save(self):
        log.debug('Saving resume data for all torrents')
        for torrent in self.core.session.get_torrents():
            if torrent.need_save_resume_data():
                self.resume_data_futures[str(torrent.info_hash())] = asyncio.Future()
                torrent.save_resume_data(
                    flags=(
                        int(lt.save_resume_flags_t.flush_disk_cache) |
                        int(lt.save_resume_flags_t.save_info_dict)
                    ),
                )
        await asyncio.gather(*self.resume_data_futures.values())

    async def load(self):
        log.info(f'Loading resume data from {self.core.state_dir}')
        for f in self.core.state_dir.iterdir():
            if f.suffix == '.resume':
                log.info(f'Found {f.name}, attempting add..')
                b = f.read_bytes()
                atp = lt.read_resume_data(b)
                try:
                    await asyncio.get_event_loop().run_in_executor(
                        None, functools.partial(self.core.session.add_torrent), atp)
                except RuntimeError as e:
                    log.error(f'Error loading resume data {f}: {e}')

                d = lt.bdecode(b)

                info_hash = binascii.hexlify(d[b'info-hash']).decode()
                self.core.torrent_data[info_hash] = {}
                for key, value in d.items():
                    if key.startswith(b'spritzle.'):
                        self.core.torrent_data[info_hash][key.decode()] = value

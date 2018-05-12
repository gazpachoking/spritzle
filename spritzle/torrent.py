#
# spritzle/torrent.py
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
import logging

log = logging.getLogger('spritzle')


class AlertException(Exception):
    def __init__(self, alert):
        self.alert = alert


class Torrent(object):
    def __init__(self, core):
        self.core = core
        self.loop = asyncio.get_event_loop()

        self.remove_torrent_futures = {}
        self.delete_torrent_futures = {}
        self.core.alert.register_handler('torrent_removed_alert', self._on_torrent_removed_alert)
        self.core.alert.register_handler('torrent_deleted_alert', self._on_torrent_deleted_alert)
        self.core.alert.register_handler('torrent_delete_failed_alert', self._on_torrent_delete_failed_alert)

    def remove(self, torrent_handle, options=0):
        info_hash = str(torrent_handle.info_hash())
        future_dict = self.delete_torrent_futures if options else self.remove_torrent_futures
        if info_hash not in future_dict:
            future_dict[info_hash] = asyncio.Future()
            self.core.session.remove_torrent(torrent_handle, options)
        return future_dict[info_hash]

    async def _on_torrent_removed_alert(self, alert):
        future = self.remove_torrent_futures.pop(str(alert.info_hash), None)
        if future:
            future.set_result(alert)

    async def _on_torrent_deleted_alert(self, alert):
        future = self.delete_torrent_futures.pop(str(alert.info_hash), None)
        if future:
            future.set_result(alert)

    async def _on_torrent_delete_failed_alert(self, alert):
        future = self.delete_torrent_futures.pop(str(alert.info_hash), None)
        if future:
            future.set_exception(AlertException(alert))

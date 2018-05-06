#
# test_resume_data.py
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
import asynctest
from pathlib import Path
import shutil

import libtorrent as lt
import pytest

resume_data_path = Path(__file__).resolve().parent / 'resource' / 'resume_data'
torrent_dir = Path(__file__).resolve().parent / 'resource' / 'torrents'


async def test_load(core):
    shutil.copy(resume_data_path / 'tmprandomfile.resume', core.state_dir)
    await core.start()
    torrents = core.session.get_torrents()
    assert len(torrents) == 1
    assert torrents[0].name() == 'tmprandomfile'
    await core.stop()


async def test_save(core):
    await core.start()
    assert len(list(core.state_dir.iterdir())) == 0
    with open(torrent_dir / 'random_one_file.torrent', mode='rb') as f:
        torrent_info = lt.torrent_info(lt.bdecode(f.read()))
    core.session.add_torrent({'ti': torrent_info})
    # We need time for the torrent added alert to come in to initiate save
    await asyncio.sleep(0.5)
    await core.stop()
    with open(core.state_dir / 'tmprandomfile.resume', mode='rb') as f:
        data = lt.bdecode(f.read())
        assert b'paused' in data
        assert data[b'info'][b'length'] == 4194304


@pytest.mark.parametrize('frequency', [0.1, 0.2])
async def test_resume_data_save_loop(core, frequency):
    """
    Verifies save resume data is called, and called as often as specified in config.
    """
    core_run_time = 0.61
    expected_runs = int(core_run_time / frequency)
    core.config['resume_data_save_frequency'] = frequency
    with asynctest.patch('spritzle.resume_data.ResumeData.save') as mock_save:
        await core.start()
        await asyncio.sleep(core_run_time)
        # Allow a bit of slop so the test isn't so fragile
        assert expected_runs - 1 <= mock_save.call_count <= expected_runs + 1
        await core.stop()

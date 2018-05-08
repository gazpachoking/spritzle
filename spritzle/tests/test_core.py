#
# test_core.py
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


# def test_save_state():
#     with tempfile.TemporaryDirectory() as tmpdir:
#         path_mock = MagicMock(return_value=os.path.join(tmpdir, "state"))
#         patch('os.path.expanduser', new=path_mock).start()
#
#         core = spritzle.core.Core()
#         assert not os.path.exists(core.get_lt_state_file_path())
#
#         core.init(os.path.join(tmpdir, "config"))
#         core.save_state()
#
#         assert os.path.exists(core.get_lt_state_file_path())


async def test_torrent_data(cli, core):
    info_hash = '44a040be6d74d8d290cd20128788864cbf770719'
    torrent_address = cli.make_url('/test_torrents/random_one_file.torrent')
    assert not core.torrent_data
    await cli.post('/torrent', data={'url': torrent_address})
    assert info_hash in core.torrent_data
    await cli.delete('/torrent/44a040be6d74d8d290cd20128788864cbf770719')
    assert not core.torrent_data
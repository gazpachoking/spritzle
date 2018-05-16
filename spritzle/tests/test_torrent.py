import asyncio
from unittest.mock import Mock

import libtorrent as lt

from spritzle.torrent import Torrent


async def test_torrent():
    torrent = Torrent(Mock())
    info_hash = 'aoeuaoeu'
    torrent_handle = Mock(**{
        'info_hash.return_value': info_hash
    })
    torrent_removed_alert = Mock(**{
        'info_hash': info_hash,
        'what.return_value': 'torrent_removed_alert',
        'category.return_value': 0
    })
    torrent_deleted_alert = Mock(**{
        'info_hash': info_hash,
        'what.return_value': 'torrent_deleted_alert',
        'category.return_value': 0
    })

    future = asyncio.ensure_future(torrent.remove(torrent_handle))
    # Need to context switch to allow the task to run
    await asyncio.sleep(0.01)
    assert not future.done()
    await torrent._on_torrent_removed_alert(torrent_removed_alert)
    await asyncio.wait_for(future, 1)
    future = asyncio.ensure_future(torrent.remove(torrent_handle, lt.options_t.delete_files))
    # Need to context switch to allow the task to run
    await asyncio.sleep(0.01)
    assert not future.done()
    await torrent._on_torrent_removed_alert(torrent_removed_alert)
    assert not future.done()
    await torrent._on_torrent_deleted_alert(torrent_deleted_alert)
    await asyncio.wait_for(future, 1)

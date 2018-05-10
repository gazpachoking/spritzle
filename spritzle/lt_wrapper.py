import asyncio

import libtorrent as lt


class Alert(object):
    def __init__(self, alert):
        self._alert = alert

    def __getattr__(self, item):
        return getattr(self._alert, item)


class AlertException(Exception):
    def __init__(self, alert):
        self.alert = Alert(alert)


class TorrentHandle(object):
    def __init__(self, torrent_handle):
        self._torrent_handle = torrent_handle

    def __getattr__(self, item):
        return getattr(self._torrent_handle, item)


class Session(object):
    def __init__(self, session):
        self._session = session
        self._add_torrent_futures = {}
        self._remove_torrent_futures = {}
        self._delete_torrent_futures = {}
        self._stats_future = None

    def async_add_torrent(self, add_torrent_params):
        add_torrent_params['flags'] = parse_flags(add_torrent_params['flags'], lt.torrent_flags)
        # TODO: We need to resolve info_hash here in order to respond to alerts
        self._session.async_add_torrent(add_torrent_params)
        self._add_torrent_futures[info_hash] = asyncio.Future()
        return self._add_torrent_futures[info_hash]

    def _on_add_torrent_alert(self, alert):
        info_hash = str(alert.handle.info_hash())
        if info_hash not in self._add_torrent_futures:
            # Torrent was added synchronously?
            return
        future = self._add_torrent_futures.pop(info_hash)
        if alert.error:
            future.set_exception(AlertException(alert))
        else:
            future.set_result(alert)

    def remove_torrent(self, torrent_handle, options=0):
        self._session.remove_torrent(torrent_handle, options)
        info_hash = str(torrent_handle.info_hash())
        future_dict = self._delete_torrent_futures if options else self._remove_torrent_futures
        if info_hash not in future_dict:
            future_dict[info_hash] = asyncio.Future()
        return future_dict[info_hash]

    def _on_torrent_removed_alert(self, alert):
        future = self._remove_torrent_futures.pop(str(alert.info_hash))
        future.set_result(alert)

    def _on_torrent_deleted_alert(self, alert):
        future = self._delete_torrent_futures.pop(str(alert.info_hash))
        future.set_result(alert)

    def _on_torrent_delete_failed_alert(self, alert):
        future = self._delete_torrent_futures.pop(str(alert.info_hash))
        future.set_exception(AlertException(alert))

    def post_session_stats(self):
        if not self._stats_future:
            self._session.post_session_stats()
            self._stats_future = asyncio.Future()
        return self._stats_future

    def _on_session_stats_alert(self, alert):
        self._stats_future.set_result(alert)
        self._stats_future = None

    def find_torrent(self, *args, **kwargs):
        return TorrentHandle(self._session.find_torrent(*args, **kwargs))

    def get_torrents(self):
        return [TorrentHandle(th) for th in self._session.get_torrents()]

    def load_state(self, state, flags=0xffffffff):
        self._session.load_state(state, parse_flags(flags, lt.save_state_flags_t))

    def save_state(self, state, flags=0xffffffff):
        self._session.save_state(parse_flags(flags, lt.save_state_flags_t))


def parse_flags(flags, enum):
    if isinstance(flags, int):
        return flags
    val = 0
    for flag in flags:
        val |= getattr(enum, flag)
    return val

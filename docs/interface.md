Interface
=========

The main interface to spritzle is REST based. This allows access from almost
any language or environment.

Session
-------

The session resource contains information about the libtorrent session.

### /session/settings
#### GET

Returns a dictionary of the session settings.

### /session/stats
#### PUT

Allows changing the session settings. New settings should be JSON format in the
body of request.

### /session/stats
#### GET

Returns a dictionary of the session stats.

**Example**

```shell
$ http GET http://localhost:8080/session/stats
HTTP/1.1 200 OK
Content-Length: 9092
Content-Type: application/json; charset=utf-8
Date: Tue, 08 May 2018 01:03:50 GMT
Server: Python/3.6 aiohttp/3.1.3

{
    "dht.dht_allocated_observers": 10,
    "dht.dht_announce_peer_in": 0,
    "dht.dht_announce_peer_out": 0,
    "dht.dht_bytes_in": 18613,
    "dht.dht_bytes_out": 8462,
    "dht.dht_find_node_in": 0,
    "dht.dht_find_node_out": 0,
    "dht.dht_get_in": 0,
    "dht.dht_get_out": 0,
    "dht.dht_get_peers_in": 0,
    "dht.dht_get_peers_out": 81,
    "dht.dht_immutable_data": 0,
    "dht.dht_invalid_announce": 0,
    "dht.dht_invalid_find_node": 0,
    "dht.dht_invalid_get": 0,
    "dht.dht_invalid_get_peers": 0,
    "dht.dht_invalid_put": 0,
    "dht.dht_invalid_sample_infohashes": 0,
    "dht.dht_messages_in": 63,
    "dht.dht_messages_in_dropped": 1,
    "dht.dht_messages_out": 81,
    "dht.dht_messages_out_dropped": 0,
    "dht.dht_mutable_data": 0,
    "dht.dht_node_cache": 61,
    "dht.dht_nodes": 95,
    "dht.dht_peers": 0,
    "dht.dht_ping_in": 0,
    "dht.dht_ping_out": 0,
    "dht.dht_put_in": 0,
    "dht.dht_put_out": 0,
    "dht.dht_sample_infohashes_in": 0,
    "dht.dht_sample_infohashes_out": 0,
    "dht.dht_torrents": 0,
    "disk.arc_mfu_ghost_size": 0,
    "disk.arc_mfu_size": 0,
    "disk.arc_mru_ghost_size": 0,
    "disk.arc_mru_size": 0,
    "disk.arc_volatile_size": 0,
    "disk.arc_write_size": 0,
    "disk.blocked_disk_jobs": 0,
    "disk.disk_blocks_in_use": 0,
    "disk.disk_hash_time": 0,
    "disk.disk_job_time": 0,
    "disk.disk_read_time": 0,
    "disk.disk_write_time": 0,
    "disk.num_blocks_cache_hits": 0,
    "disk.num_blocks_hashed": 0,
    "disk.num_blocks_read": 0,
    "disk.num_blocks_written": 0,
    "disk.num_fenced_check_fastresume": 0,
    "disk.num_fenced_clear_piece": 0,
    "disk.num_fenced_delete_files": 0,
    "disk.num_fenced_file_priority": 0,
    "disk.num_fenced_flush_hashed": 0,
    "disk.num_fenced_flush_piece": 0,
    "disk.num_fenced_flush_storage": 0,
    "disk.num_fenced_hash": 0,
    "disk.num_fenced_load_torrent": 0,
    "disk.num_fenced_move_storage": 0,
    "disk.num_fenced_read": 0,
    "disk.num_fenced_release_files": 0,
    "disk.num_fenced_rename_file": 0,
    "disk.num_fenced_save_resume_data": 0,
    "disk.num_fenced_stop_torrent": 0,
    "disk.num_fenced_tick_storage": 0,
    "disk.num_fenced_trim_cache": 0,
    "disk.num_fenced_write": 0,
    "disk.num_jobs": 0,
    "disk.num_read_back": 0,
    "disk.num_read_jobs": 0,
    "disk.num_read_ops": 0,
    "disk.num_running_disk_jobs": 0,
    "disk.num_running_threads": 0,
    "disk.num_write_jobs": 0,
    "disk.num_write_ops": 0,
    "disk.num_writing_threads": 0,
    "disk.pinned_blocks": 0,
    "disk.queued_disk_jobs": 0,
    "disk.queued_write_bytes": 0,
    "disk.read_cache_blocks": 0,
    "disk.request_latency": 0,
    "disk.write_cache_blocks": 0,
    "net.has_incoming_connections": 0,
    "net.limiter_down_bytes": 0,
    "net.limiter_down_queue": 0,
    "net.limiter_up_bytes": 0,
    "net.limiter_up_queue": 0,
    "net.on_accept_counter": 0,
    "net.on_disk_counter": 0,
    "net.on_disk_queue_counter": 0,
    "net.on_lsd_counter": 0,
    "net.on_lsd_peer_counter": 0,
    "net.on_read_counter": 0,
    "net.on_tick_counter": 50,
    "net.on_udp_counter": 60,
    "net.on_write_counter": 0,
    "net.recv_bytes": 0,
    "net.recv_failed_bytes": 0,
    "net.recv_ip_overhead_bytes": 1764,
    "net.recv_payload_bytes": 0,
    "net.recv_redundant_bytes": 0,
    "net.recv_tracker_bytes": 0,
    "net.sent_bytes": 0,
    "net.sent_ip_overhead_bytes": 2268,
    "net.sent_payload_bytes": 0,
    "net.sent_tracker_bytes": 0,
    "peer.aborted_peers": 0,
    "peer.addrinuse_peers": 0,
    "peer.banned_for_hash_failure": 0,
    "peer.broken_pipe_peers": 0,
    "peer.buffer_peers": 0,
    "peer.cancelled_piece_requests": 0,
    "peer.choked_piece_requests": 0,
    "peer.connaborted_peers": 0,
    "peer.connect_timeouts": 0,
    "peer.connection_attempt_loops": 0,
    "peer.connection_attempts": 0,
    "peer.connrefused_peers": 0,
    "peer.connreset_peers": 0,
    "peer.disconnected_peers": 0,
    "peer.eof_peers": 0,
    "peer.error_encrypted_peers": 0,
    "peer.error_incoming_peers": 0,
    "peer.error_outgoing_peers": 0,
    "peer.error_peers": 0,
    "peer.error_rc4_peers": 0,
    "peer.error_tcp_peers": 0,
    "peer.error_utp_peers": 0,
    "peer.incoming_connections": 0,
    "peer.invalid_arg_peers": 0,
    "peer.invalid_piece_requests": 0,
    "peer.max_piece_requests": 0,
    "peer.no_access_peers": 0,
    "peer.no_memory_peers": 0,
    "peer.notconnected_peers": 0,
    "peer.num_banned_peers": 0,
    "peer.num_http_proxy_peers": 0,
    "peer.num_i2p_peers": 0,
    "peer.num_peers_connected": 0,
    "peer.num_peers_down_disk": 0,
    "peer.num_peers_down_interested": 0,
    "peer.num_peers_down_requests": 0,
    "peer.num_peers_down_unchoked": 0,
    "peer.num_peers_end_game": 0,
    "peer.num_peers_half_open": 0,
    "peer.num_peers_up_disk": 0,
    "peer.num_peers_up_interested": 0,
    "peer.num_peers_up_requests": 0,
    "peer.num_peers_up_unchoked": 0,
    "peer.num_peers_up_unchoked_all": 0,
    "peer.num_peers_up_unchoked_optimistic": 0,
    "peer.num_socks5_peers": 0,
    "peer.num_ssl_http_proxy_peers": 0,
    "peer.num_ssl_peers": 0,
    "peer.num_ssl_socks5_peers": 0,
    "peer.num_ssl_utp_peers": 0,
    "peer.num_tcp_peers": 0,
    "peer.num_utp_peers": 0,
    "peer.perm_peers": 0,
    "peer.piece_rejects": 0,
    "peer.piece_requests": 0,
    "peer.timeout_peers": 0,
    "peer.too_many_peers": 0,
    "peer.transport_timeout_peers": 0,
    "peer.uninteresting_peers": 0,
    "peer.unreachable_peers": 0,
    "picker.end_game_piece_picks": 0,
    "picker.hash_fail_piece_picks": 0,
    "picker.incoming_piece_picks": 0,
    "picker.incoming_redundant_piece_picks": 0,
    "picker.interesting_piece_picks": 0,
    "picker.piece_picker_busy_loops": 0,
    "picker.piece_picker_partial_loops": 0,
    "picker.piece_picker_rand_loops": 0,
    "picker.piece_picker_rand_start_loops": 0,
    "picker.piece_picker_rare_loops": 0,
    "picker.piece_picker_reverse_rare_loops": 0,
    "picker.piece_picker_sequential_loops": 0,
    "picker.piece_picker_suggest_loops": 0,
    "picker.reject_piece_picks": 0,
    "picker.snubbed_piece_picks": 0,
    "picker.unchoke_piece_picks": 0,
    "ses.non_filter_torrents": 0,
    "ses.num_checking_torrents": 0,
    "ses.num_downloading_torrents": 1,
    "ses.num_error_torrents": 0,
    "ses.num_have_pieces": 0,
    "ses.num_incoming_allowed_fast": 0,
    "ses.num_incoming_bitfield": 0,
    "ses.num_incoming_cancel": 0,
    "ses.num_incoming_choke": 0,
    "ses.num_incoming_dht_port": 0,
    "ses.num_incoming_ext_handshake": 0,
    "ses.num_incoming_extended": 0,
    "ses.num_incoming_have": 0,
    "ses.num_incoming_have_all": 0,
    "ses.num_incoming_have_none": 0,
    "ses.num_incoming_interested": 0,
    "ses.num_incoming_metadata": 0,
    "ses.num_incoming_not_interested": 0,
    "ses.num_incoming_pex": 0,
    "ses.num_incoming_piece": 0,
    "ses.num_incoming_reject": 0,
    "ses.num_incoming_request": 0,
    "ses.num_incoming_suggest": 0,
    "ses.num_incoming_unchoke": 0,
    "ses.num_outgoing_allowed_fast": 0,
    "ses.num_outgoing_bitfield": 0,
    "ses.num_outgoing_cancel": 0,
    "ses.num_outgoing_choke": 0,
    "ses.num_outgoing_dht_port": 0,
    "ses.num_outgoing_ext_handshake": 0,
    "ses.num_outgoing_extended": 0,
    "ses.num_outgoing_have": 0,
    "ses.num_outgoing_have_all": 0,
    "ses.num_outgoing_have_none": 0,
    "ses.num_outgoing_interested": 0,
    "ses.num_outgoing_metadata": 0,
    "ses.num_outgoing_not_interested": 0,
    "ses.num_outgoing_pex": 0,
    "ses.num_outgoing_piece": 0,
    "ses.num_outgoing_reject": 0,
    "ses.num_outgoing_request": 0,
    "ses.num_outgoing_suggest": 0,
    "ses.num_outgoing_unchoke": 0,
    "ses.num_piece_failed": 0,
    "ses.num_piece_passed": 0,
    "ses.num_queued_download_torrents": 0,
    "ses.num_queued_seeding_torrents": 0,
    "ses.num_seeding_torrents": 0,
    "ses.num_stopped_torrents": 0,
    "ses.num_total_pieces_added": 0,
    "ses.num_unchoke_slots": 8,
    "ses.num_upload_only_torrents": 0,
    "ses.torrent_evicted_counter": 0,
    "ses.waste_piece_cancelled": 0,
    "ses.waste_piece_closing": 0,
    "ses.waste_piece_end_game": 0,
    "ses.waste_piece_seed": 0,
    "ses.waste_piece_timed_out": 0,
    "ses.waste_piece_unknown": 0,
    "sock_bufs.socket_recv_size10": 0,
    "sock_bufs.socket_recv_size11": 0,
    "sock_bufs.socket_recv_size12": 0,
    "sock_bufs.socket_recv_size13": 0,
    "sock_bufs.socket_recv_size14": 0,
    "sock_bufs.socket_recv_size15": 0,
    "sock_bufs.socket_recv_size16": 0,
    "sock_bufs.socket_recv_size17": 0,
    "sock_bufs.socket_recv_size18": 0,
    "sock_bufs.socket_recv_size19": 0,
    "sock_bufs.socket_recv_size20": 0,
    "sock_bufs.socket_recv_size3": 0,
    "sock_bufs.socket_recv_size4": 0,
    "sock_bufs.socket_recv_size5": 0,
    "sock_bufs.socket_recv_size6": 0,
    "sock_bufs.socket_recv_size7": 0,
    "sock_bufs.socket_recv_size8": 0,
    "sock_bufs.socket_recv_size9": 0,
    "sock_bufs.socket_send_size10": 0,
    "sock_bufs.socket_send_size11": 0,
    "sock_bufs.socket_send_size12": 0,
    "sock_bufs.socket_send_size13": 0,
    "sock_bufs.socket_send_size14": 0,
    "sock_bufs.socket_send_size15": 0,
    "sock_bufs.socket_send_size16": 0,
    "sock_bufs.socket_send_size17": 0,
    "sock_bufs.socket_send_size18": 0,
    "sock_bufs.socket_send_size19": 0,
    "sock_bufs.socket_send_size20": 0,
    "sock_bufs.socket_send_size3": 0,
    "sock_bufs.socket_send_size4": 0,
    "sock_bufs.socket_send_size5": 0,
    "sock_bufs.socket_send_size6": 0,
    "sock_bufs.socket_send_size7": 0,
    "sock_bufs.socket_send_size8": 0,
    "sock_bufs.socket_send_size9": 0,
    "utp.num_utp_close_wait": 0,
    "utp.num_utp_connected": 0,
    "utp.num_utp_deleted": 0,
    "utp.num_utp_fin_sent": 0,
    "utp.num_utp_idle": 0,
    "utp.num_utp_syn_sent": 0,
    "utp.utp_fast_retransmit": 0,
    "utp.utp_invalid_pkts_in": 0,
    "utp.utp_packet_loss": 0,
    "utp.utp_packet_resend": 0,
    "utp.utp_packets_in": 0,
    "utp.utp_packets_out": 0,
    "utp.utp_payload_pkts_in": 0,
    "utp.utp_payload_pkts_out": 0,
    "utp.utp_redundant_pkts_in": 0,
    "utp.utp_samples_above_target": 0,
    "utp.utp_samples_below_target": 0,
    "utp.utp_timeout": 0
}
```

### /session/dht
#### GET

Returns a boolean indicating if DHT is running or not.

```shell
$ http GET http://localhost:8080/session/dht
HTTP/1.1 200 OK
Content-Length: 4
Content-Type: application/json; charset=utf-8
Date: Tue, 08 May 2018 01:04:49 GMT
Server: Python/3.6 aiohttp/3.1.3

true
```

Torrent
--------

A torrent resource contains all the information you would need to know about a torrent.

### /torrent
#### GET

Returns a list of all info-hashes in the session.

**Example**

```shell
$ http GET http://localhost:8080/torrent
HTTP/1.1 200 OK
Content-Length: 44
Content-Type: application/json; charset=utf-8
Date: Tue, 08 May 2018 01:05:42 GMT
Server: Python/3.6 aiohttp/3.1.3

[
    "44a040be6d74d8d290cd20128788864cbf770719"
]
```

#### POST

Add a torrent to the session. The body of the request should be a JSON encoded dictionary.

There are three ways to add a torrent to the session using one of these three
keys: **file**, **url** or **info_hash**.

Any libtorrent options can also be passed, see
https://libtorrent.org/reference-Core.html#add_torrent_params for reference.

The **spritzle.tags** key can also be passed as a list, containing spritzle tags which should apply to this torrent.

Upon success, you will receive a 201 response and a dictionary with the info_hash in the body. The LOCATION
header will also be set in the response for the new torrent resource.

##### File Upload

Adding a torrent by uploading a torrent file requires the use of a multipart/form-data post with the file contents keyed as **file**.

**Example**

```shell
$ http POST http://localhost:8080/torrent file="$(base64 random_one_file.torrent)" save_path=/tmp
HTTP/1.1 201 Created
Content-Length: 57
Content-Type: application/json; charset=utf-8
Date: Tue, 08 May 2018 01:08:43 GMT
Location: http://localhost:8080/torrent/44a040be6d74d8d290cd20128788864cbf770719
Server: Python/3.6 aiohttp/3.1.3

{
    "info_hash": "44a040be6d74d8d290cd20128788864cbf770719"
}
```

##### URL

Adding a torrent by url is done by setting the **url** key.

**Example**

```shell
$ http POST http://localhost:8080/torrent url=https://www.archlinux.org/releng/releases/2016.02.01/torrent/ save_path=/tmp
HTTP/1.1 201 Created
Content-Length: 57
Content-Type: application/json; charset=utf-8
Date: Tue, 08 May 2018 01:12:01 GMT
Location: http://localhost:8080/torrent/88066b90278f2de655ee2dd44e784c340b54e45c
Server: Python/3.6 aiohttp/3.1.3

{
    "info_hash": "88066b90278f2de655ee2dd44e784c340b54e45c"
}
```

##### Info-hash

Adding a torrent by info-hash is done by setting the **info_hash** key.

**Example**

```shell
$ http POST http://localhost:8080/torrent info_hash=88066b90278f2de655ee2dd44e784c340b54e45c save_path=/tmp
HTTP/1.1 201 Created
Content-Length: 57
Content-Type: application/json; charset=utf-8
Date: Tue, 08 May 2018 01:15:07 GMT
Location: http://localhost:8080/torrent/88066b90278f2de655ee2dd44e784c340b54e45c
Server: Python/3.6 aiohttp/3.1.3

{
    "info_hash": "88066b90278f2de655ee2dd44e784c340b54e45c"
}
```

#### DELETE

Remove all torrents from the session.

Optionally, the downloaded files can be deleted when the torrent is removed by adding
the **delete_files** key to the query string.

**Example**
```shell
$ http DELETE http://localhost:8080/torrent?delete_files
HTTP/1.1 200 OK
Content-Length: 0
Content-Type: application/octet-stream
Date: Tue, 08 May 2018 01:16:03 GMT
Server: Python/3.6 aiohttp/3.1.3
```

### /torrent/\<info-hash\>
#### GET

Returns a status dictionary for the torrent.

**Example**

```shell
$ http GET http://localhost:8080/torrent/44a040be6d74d8d290cd20128788864cbf770719
HTTP/1.1 200 OK
Content-Length: 4059
Content-Type: application/json; charset=utf-8
Date: Tue, 08 May 2018 01:18:07 GMT
Server: Python/3.6 aiohttp/3.1.3

{
    "active_duration": "0.0",
    "active_time": 0,
    "added_time": 1525742268,
    "all_time_download": 0,
    "all_time_upload": 0,
    "announce_interval": "0.0",
    "announcing_to_dht": false,
    "announcing_to_lsd": false,
    "announcing_to_trackers": false,
    "auto_managed": false,
    "block_size": 16384,
    "completed_time": 0,
    "connect_candidates": 0,
    "connections_limit": -1,
    "current_tracker": "",
    "distributed_copies": 0.0,
    "distributed_fraction": 0,
    "distributed_full_copies": 0,
    "down_bandwidth_queue": 0,
    "download_payload_rate": 0,
    "download_rate": 0,
    "error_file": 0,
    "finished_duration": "0.0",
    "finished_time": 0,
    "flags": 24,
    "has_incoming": false,
    "has_metadata": true,
    "info_hash": "44a040be6d74d8d290cd20128788864cbf770719",
    "ip_filter_applies": true,
    "is_finished": false,
    "is_loaded": true,
    "is_seeding": false,
    "last_scrape": -1,
    "last_seen_complete": 0,
    "list_peers": 0,
    "list_seeds": 0,
    "moving_storage": false,
    "name": "tmprandomfile",
    "need_save_resume": true,
    "next_announce": "0.0",
    "num_complete": -1,
    "num_connections": 0,
    "num_incomplete": -1,
    "num_peers": 0,
    "num_pieces": 0,
    "num_seeds": 0,
    "num_uploads": 0,
    "paused": true,
    "pieces": [
        false,
        false,
        false,
        false
    ],
    "priority": 0,
    "progress": 0.0,
    "progress_ppm": 0,
    "queue_position": 0,
    "save_path": "/tmp",
    "seed_mode": false,
    "seed_rank": 0,
    "seeding_duration": "0.0",
    "seeding_time": 0,
    "sequential_download": false,
    "share_mode": false,
    "spritzle.tags": [],
    "state": "checking_files",
    "stop_when_ready": false,
    "super_seeding": false,
    "time_since_download": 19,
    "time_since_upload": 19,
    "total_done": 0,
    "total_download": 0,
    "total_failed_bytes": 0,
    "total_payload_download": 0,
    "total_payload_upload": 0,
    "total_redundant_bytes": 0,
    "total_upload": 0,
    "total_wanted": 4194304,
    "total_wanted_done": 0,
    "up_bandwidth_queue": 0,
    "upload_mode": false,
    "upload_payload_rate": 0,
    "upload_rate": 0,
    "uploads_limit": -1,
    "verified_pieces": []
}
```

#### DELETE

Remove torrent from the session.

Optionally, the downloaded files can be deleted when the torrent is removed by adding
the **delete_files** key to the query string.

**Example**

```shell
$ http DELETE http://localhost:8080/torrent/88066b90278f2de655ee2dd44e784c340b54e45c?delete_files
HTTP/1.1 200 OK
Content-Length: 0
Content-Type: application/octet-stream
Date: Tue, 08 May 2018 01:12:36 GMT
Server: Python/3.6 aiohttp/3.1.3
```

Core
----
### /core
#### DELETE

Initiates Spritzle shutdown.

**Example**

```shell
$ http DELETE http://localhost:8080/core
HTTP/1.1 200 OK
Content-Length: 0
Content-Type: application/octet-stream
Date: Tue, 08 May 2018 01:21:31 GMT
Server: Python/3.6 aiohttp/3.1.3
```

from functools import partial
import tempfile
import logging
from pathlib import Path
import shutil
from unittest.mock import patch

import aiohttp.web
import pytest

from spritzle.core import Core
from spritzle.config import Config
from spritzle.main import setup_app

pytest_plugins = 'aiohttp.pytest_plugin'


@pytest.fixture(scope='function')
def core(loop):
    config = Config(in_memory=True, config_dir='/tmp')
    state_dir = Path(tempfile.mkdtemp(prefix='spritzle-test'))
    core = Core(config, state_dir)
    settings = {
        'enable_upnp': False,
        'enable_natpmp': False,
        'enable_lsd': False,
        'enable_dht': False,
        'anonymous_mode': True,
        'alert_mask': 0,
        'stop_tracker_timeout': 0,
    }
    with patch.object(core, 'start', partial(core.start, settings=settings)):
        yield core
    shutil.rmtree(str(state_dir))


@pytest.fixture
def app(core):
    app = aiohttp.web.Application()
    log = logging.getLogger('spritzle')
    logging.basicConfig(level=logging.DEBUG)
    setup_app(app, core, log)
    return app


@pytest.fixture
def cli(loop, app, aiohttp_client):
    return loop.run_until_complete(
        aiohttp_client(app, server_kwargs={'host': 'localhost', 'port': 8080})
    )

import json
import asyncio
import functools
from unittest.mock import MagicMock

from spritzle.config import Config


def run_until_complete(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        coro = asyncio.coroutine(f)
        future = coro(*args, **kwargs)
        loop = asyncio.get_event_loop()
        if not loop.is_running():
            return loop.run_until_complete(future)
        else:
            return asyncio.ensure_future(future)

    return wrapper


async def json_response(cr):
    response = await cr
    assert response.content_type == 'application/json'
    return json.loads(response.text), response


async def create_mock_request(core=None, config=None):
    config = Config(in_memory=True, config_dir='/tmp', initial=config)
    core.config = config
    request = MagicMock()
    request.app = {
        'spritzle.core': core,
        'spritzle.config': config,
    }

    return request

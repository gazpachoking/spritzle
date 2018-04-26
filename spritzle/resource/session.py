#
# spritzle/session.py
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

from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/session/settings')
async def get_session_settings(request):
    core = request.app['spritzle.core']
    settings = core.session.get_settings()
    return web.json_response(settings)


@routes.patch('/session/settings')
async def get_session_settings(request):
    core = request.app['spritzle.core']
    settings = core.session.get_settings()
    new_settings = await request.json()
    settings.update(new_settings)
    core.session.apply_settings(settings)
    return web.Response()


@routes.get('/session/stats')
async def get_session_stats(request):
    core = request.app['spritzle.core']
    stats = await core.get_session_stats()
    return web.json_response(stats)


@routes.get('/session/dht')
async def get_session_dht(request):
    core = request.app['spritzle.core']
    return web.json_response(core.session.is_dht_running())

"""Matrix Webhook utils."""

import logging
from collections import defaultdict
from http import HTTPStatus

from aiohttp import web
from nio import AsyncClient
from nio.exceptions import LocalProtocolError
from nio.responses import JoinError, RoomSendError

from . import conf

ERROR_MAP = defaultdict(
    lambda: HTTPStatus.INTERNAL_SERVER_ERROR,
    {
        "M_FORBIDDEN": HTTPStatus.FORBIDDEN,
        "M_CONSENT_NOT_GIVEN": HTTPStatus.FORBIDDEN,
    },
)
LOGGER = logging.getLogger("matrix_webhook.utils")
CLIENT = AsyncClient(conf.MATRIX_URL, conf.MATRIX_ID)


def error_map(resp):
    """Map response errors to HTTP status."""
    if resp.status_code == "M_UNKNOWN":
        # in this case, we should directly consider the HTTP status from the response
        # ref. https://matrix.org/docs/spec/client_server/r0.6.1#api-standards
        return resp.transport_response.status
    return ERROR_MAP[resp.status_code]


def create_json_response(status, ret):
    """Create a JSON response."""
    msg = f"Creating json response: {status=}, {ret=}"
    LOGGER.debug(msg)
    response_data = {"status": status, "ret": ret}
    return web.json_response(response_data, status=status)


async def join_room(room_id):
    """Try to join the room."""
    msg = f"Join room {room_id=}"
    LOGGER.debug(msg)

    for _ in range(10):
        try:
            resp = await CLIENT.join(room_id)
            if isinstance(resp, JoinError):
                if resp.status_code == "M_UNKNOWN_TOKEN":
                    LOGGER.warning("Reconnecting")
                    if conf.MATRIX_PW:
                        await CLIENT.login(conf.MATRIX_PW)
                else:
                    return create_json_response(error_map(resp), resp.message)
            else:
                return None
        except LocalProtocolError as e:
            msg = f"Send error: {e}"
            LOGGER.error(msg)
            LOGGER.warning("Reconnecting")
            if conf.MATRIX_PW:
                await CLIENT.login(conf.MATRIX_PW)
        LOGGER.warning("Trying again")
    return create_json_response(HTTPStatus.GATEWAY_TIMEOUT, "Homeserver not responding")


async def send_room_message(room_id, content):
    """Send a message to a room."""
    msg = f"Sending room message in {room_id=}: {content=}"
    LOGGER.debug(msg)

    for _ in range(10):
        try:
            resp = await CLIENT.room_send(
                room_id=room_id,
                message_type="m.room.message",
                content=content,
            )
            if isinstance(resp, RoomSendError):
                if resp.status_code == "M_UNKNOWN_TOKEN":
                    LOGGER.warning("Reconnecting")
                    if conf.MATRIX_PW:
                        await CLIENT.login(conf.MATRIX_PW)
                else:
                    return create_json_response(error_map(resp), resp.message)
            else:
                return create_json_response(HTTPStatus.OK, "OK")
        except LocalProtocolError as e:
            msg = f"Send error: {e}"
            LOGGER.error(msg)
            LOGGER.warning("Reconnecting")
            if conf.MATRIX_PW:
                await CLIENT.login(conf.MATRIX_PW)
        LOGGER.warning("Trying again")
    return create_json_response(HTTPStatus.GATEWAY_TIMEOUT, "Homeserver not responding")

# ruff: noqa: D100, D102, D103, S101, S106

import pytest
from httpx import AsyncClient
from httpx import HTTPError
from minimal_activitypub.client_2_server import ActivityPub
from minimal_activitypub.client_2_server import NetworkError
from minimal_activitypub.client_2_server import ServerError
from pytest_httpx import HTTPXMock


@pytest.mark.asyncio
async def test_verify_creds_ok(httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(json={}, headers={})
    client = AsyncClient()
    instance = ActivityPub(
        instance="https://instance.url",
        session=client,
        access_token="access_token",
    )
    response = await instance.verify_credentials()
    assert response is not None


@pytest.mark.asyncio
async def test_verify_creds_server_error(httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        status_code=500,
        json={"error": "System Error Occurred"},
    )
    client = AsyncClient()
    instance = ActivityPub(
        instance="https://instance.url",
        session=client,
        access_token="access_token",
    )
    with pytest.raises(ServerError):
        _response = await instance.verify_credentials()


@pytest.mark.asyncio
async def test_verify_creds_network_error(httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_exception(HTTPError("Unable to read within timeout"))
    client = AsyncClient()
    instance = ActivityPub(
        instance="https://instance.url",
        session=client,
        access_token="access_token",
    )
    with pytest.raises(NetworkError):
        _response = await instance.verify_credentials()

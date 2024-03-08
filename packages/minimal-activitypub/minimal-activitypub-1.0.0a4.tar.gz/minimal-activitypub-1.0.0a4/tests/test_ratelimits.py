# ruff: noqa: D100, D102, D103, S101, S106
import datetime

import pytest
from httpx import AsyncClient
from minimal_activitypub.client_2_server import ActivityPub
from minimal_activitypub.client_2_server import RatelimitError


@pytest.mark.asyncio
async def test_update_ratelimit() -> None:
    client = AsyncClient()
    instance = ActivityPub(
        instance="https://instance.url",
        session=client,
        access_token="access_token",
    )
    headers = {
        "X-RateLimit-Limit": "300",
        "X-RateLimit-Remaining": "0",
        "X-RateLimit-Reset": "2024-05-05T19:00:18.123448+10",
    }

    instance._update_ratelimit(headers=headers)

    assert instance.ratelimit_limit == 300
    assert instance.ratelimit_remaining == 0
    assert isinstance(instance.ratelimit_reset, datetime.datetime)

    with pytest.raises(RatelimitError):
        await instance._pre_call_checks()

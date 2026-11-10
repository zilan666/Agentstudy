import asyncio

import pytest

from agent.fetcher import FetchError, fetch_all


def test_fetch_all_returns_results_in_order():
    results = asyncio.run(fetch_all([3, 1, 2], timeout=1.0))
    assert results == ["spot-3", "spot-1", "spot-2"]


def test_fetch_all_rejects_invalid_spot_id():
    with pytest.raises(FetchError, match="Invalid spot ID"):
        asyncio.run(fetch_all([1, 0], timeout=1.0))


def test_fetch_all_times_out():
    with pytest.raises(FetchError, match="timed out"):
        asyncio.run(fetch_all([1], timeout=0.01))


def test_fetch_all_uses_safe_default_timeout():
    results = asyncio.run(fetch_all([1, 2, 3]))

    assert results == ["spot-1", "spot-2", "spot-3"]

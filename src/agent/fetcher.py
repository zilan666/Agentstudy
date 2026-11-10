import asyncio


class FetchError(Exception):
    """Raised when a fetch operation fails."""


async def fetch_spot(spot_id: int, delay: float = 0.1) -> str:

    if spot_id <= 0:
        raise FetchError(f"Invalid spot ID: {spot_id}")
    await asyncio.sleep(delay)
    return f"spot-{spot_id}"


async def fetch_all(spot_ids: list[int], timeout: float = 1.0) -> list[str]:
    try:
        async with asyncio.timeout(timeout):
            return await asyncio.gather(*(fetch_spot(spot_id) for spot_id in spot_ids))
    except TimeoutError as exc:
        raise FetchError(f"fetch timed out after {timeout} seconds") from exc

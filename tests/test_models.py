import pytest
from pydantic import ValidationError

from agent.models import ScenicSpot


def test_valid_scenic_spot():
    spot = ScenicSpot(id=1, name="平遥古城", city="晋中", rating=4.8)
    assert spot.ticket_price == 0.0
    assert spot.tags == []

def test_rejects_invalid_id():
    with pytest.raises(ValidationError):
        ScenicSpot(id=0, name="平遥古城", city="晋中", rating=4.8)

def test_rejects_empty_name():
    with pytest.raises(ValidationError):
        ScenicSpot(
            id=1,
            name="",
            city="晋中",
            rating=4.8,
        )

def test_rejects_too_long_city():
    with pytest.raises(ValidationError):
        ScenicSpot(
            id=1,
            name="平遥古城",
            city="这是一个特别特别特别特别特别特别长的城市名",
            rating=4.8,
        )

def test_rejects_too_high_rating():
    with pytest.raises(ValidationError):
        ScenicSpot(
            id=1,
            name="平遥古城",
            city="晋中",
            rating=5.1,
        )

def test_rejects_negative_ticket_price():
    with pytest.raises(ValidationError):
        ScenicSpot(
            id=1,
            name="平遥古城",
            city="晋中",
            rating=4.8,
            ticket_price=-1,
        )


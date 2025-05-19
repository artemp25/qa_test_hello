from src.logic import can_enter_concert
import pytest

@pytest.mark.parametrize("age, has_ticket, expected", [
    (20, True, True),
    (16, True, False),
    (25, False, False),
    (18, True, True),
])
def test_concert(age, has_ticket, expected):
    assert can_enter_concert(age, has_ticket) == expected

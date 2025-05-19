from src.logic import can_enter_concert

def test_allowed_adult_with_ticket():
    assert can_enter_concert(20, True)

def test_underage_with_ticket():
    assert not can_enter_concert(16, True)

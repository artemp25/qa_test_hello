# Это функция, которую будем тестировать
def can_enter_concert(age, has_ticket):
    return age >= 18 and has_ticket

# Тест 1
def test_allowed_adult_with_ticket():
    assert can_enter_concert(20, True) == True

# Тест 2
def test_underage_with_ticket():
    assert can_enter_concert(16, True) == False

# Тест 3
def test_adult_without_ticket():
    assert can_enter_concert(25, False) == False

# Тест 4
def test_exactly_18_with_ticket():
    assert can_enter_concert(18, True) == True

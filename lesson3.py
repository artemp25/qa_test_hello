# Функция, которую будем тестировать
def can_enter_concert(age, has_ticket):
    if age >= 18 and has_ticket:
        return True
    else:
        return False

# Тест 1
assert can_enter_concert(21, True) == True

# Тест 2
assert can_enter_concert(17, True) == False

# Тест 3
assert can_enter_concert(19, False) == False

# Тест 4
assert can_enter_concert(18, True) == True

print("Все проверки пройдены успешно ✅")

use_age = 21
has_ticket = True

if use_age >= 18 and has_ticket:
    print("Пользователь допущен на концерт")
else:
    print("Доступ запрещён")

def can_user_enter(age, ticket):
    if age >= 18 and ticket:
        return "✅ Пользователь допущен"
    else:
        return "❌ Доступ запрещён"

print(can_user_enter(21, True))
print(can_user_enter(17, False))
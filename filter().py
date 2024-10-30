# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
#
#
# print(list(even_numbers))
# # [2, 4, 6]

# test_cases = [
#    {"id": 1, "category": "UI", "description": "Тестирование интерфейса"},
#    {"id": 2, "category": "Backend", "description": "Тестирование API"},
#    {"id": 3, "category": "UI", "description": "Проверка элементов управления"},
# ]
#
#
# ui_tests = filter(lambda x: x["category"] == "UI", test_cases)
# print(list(ui_tests))
# # [{'id': 1, 'category': 'UI', 'description': 'Тестирование интерфейса'},
# # {'id': 3, 'category': 'UI', 'description': 'Проверка элементов управления'}]

tests = [
    {"name": "test_login", "executed": True},
    {"name": "test_registration", "executed": False},
    {"name": "test_password_reset", "executed": True},
    {"name": "test_profile_update", "executed": False},
]

pending_tests = filter(lambda x: not x["executed"], tests)

for test in pending_tests:
    print(f"Running test: {test['name']}")
    # Здесь может быть логика выполнения теста
    # ...

# Running test: test_registration
# Running test: test_profile_update
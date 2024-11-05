from functools import partial
def test_api(endpoint, method, params):
    print('Test started for {}...'.format(endpoint))
    # Остальной код для тестирования
    ...

# Создаем новую функцию, указывая исходную и какой параметр сделать статическим:
test_get = partial(test_api, method="GET")

# И теперь используем функцию без необходимости указания параметра method:
test_get(endpoint="/api/v1/users", params={})
test_get(endpoint="/api/v1/orders", params={})

# Test started for /api/v1/users...
# Test started for /api/v1/orders...
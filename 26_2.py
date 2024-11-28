def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@do_twice
def test_twice_without_params():
    print("Этот вызов без параметров")


@do_twice
def test_twice_2_params(str1, str2):
    print("В этой функции 2 параметра - {0} и {1}".format(str1, str2))

@do_twice
def test_twice(str):
    print("Этот вызов возвращает строку {0}".format(str))

test_twice_without_params()
test_twice_2_params("1", "2")
test_twice("single")

# Этот вызов без параметров
# Этот вызов без параметров
# В этой функции 2 параметра - 1 и 2
# В этой функции 2 параметра - 1 и 2
# Этот вызов возвращает строку single
# Этот вызов возвращает строку single

@do_twice
def test_twice(str):
    print("Этот вызов возвращает строку {0}".format(str))
    return "Done"

decorated_value = test_twice("single")
# Этот вызов возвращает строку single
# Этот вызов возвращает строку single
print(decorated_value)
# None




def do_twice_with_return(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@do_twice_with_return
def test_twice(str):
    print("Этот вызов возвращает строку {0}".format(str))
    return "Done"

decorated_value = test_twice("single")
print(decorated_value)
# Этот вызов возвращает строку single
# Этот вызов возвращает строку single
# Done
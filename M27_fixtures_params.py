import pytest


def python_string_slicer(str):
   if len(str) < 50 or "python" in str:
       return str
   else:
       return str[0:50]


@pytest.fixture(scope="function", params=[
   ("Короткая строка", "Короткая строка"),
   ("Длинная строка, не то чтобы прям очень длинная, но достаточно для нашего теста, и в ней нет названия языка"
    , "Длинная строка, не то чтобы прям очень длинная, но"),
   ("Короткая строка со словом python", "Короткая строка со словом python"),
   ("Длинная строка, нам достаточно будет для проверки, и в ней есть слово python"
    , "Длинная строка, нам достаточно будет для проверки, и в ней есть слово python"),
], ids=["len < 50", "len > 50", "len < 50 contains python", "len > 50 contains python"])
def param_fun(request):
   return request.param


def test_python_string_slicer(param_fun):
   (input, expected_output) = param_fun
   result = python_string_slicer(input)
   print ("Входная строка: {0}\nВыходная строка: {1}\nОжидаемое значение: {2}".format(input, result, expected_output))
   assert result == expected_output
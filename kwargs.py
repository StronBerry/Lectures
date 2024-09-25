# def func(a, b, c=0, d=1, *args, e, f, **kwargs):
#     func(1, 2, 3, 4, 5, 6, e=7, f=8, g=9, h=10)
# #
# list1 = [1, 2, 3]
# tuple1 = (4, 5, 6)
# list2 = [True, False]
# tuple2 = ('O', 'OX')
# result = [*list1, *tuple1, *list2, *tuple2]
# print(result)
# # [1, 2, 3, 4, 5, 6, True, False, 'O', 'OX']

# def my_func(**kwargs):
#    print(type(kwargs))
#    print(kwargs)
#
# my_func(body={"name": "John"}, headers={"Content-Type": "application/json"})
# # <class 'dict'>
# # {'body': {'name': 'John'}, 'headers': {'Content-Type': 'application/json'}}
#
# def send_request(url, method, **kwargs):
#    print(f"Отправка {method}-запроса на {url} с параметрами {kwargs}")
#
# send_request('https://my-api.com/resources', 'POST', body={"name": "John"}, headers={"Content-Type": "application/json"})
# # Отправка POST-запроса на https://my-api.com/resources с параметрами {'body': {'name': 'John'}, 'headers': {'Content-Type': 'application/json'}}


# dict1 = {'1':891239912, '2':19245912, '3': 12300123}
# dict2 = {'4':81249912, '5':678912, '6': 123003453}
# print({**dict1, **dict2})
# # {'1': 891239912, '2': 19245912, '3': 12300123, '4': 81249912, '5': 678912, '6': 123003453}
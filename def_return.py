def count_elements(input_list):
   if type(input_list) not in (list, tuple, str):
       return "Недопустимый тип переданного аргумента"
   print('Начало вычисления...')
   dict1 = {}
   for i in input_list:
       if i in dict1:
           dict1[i] += 1
       else:
           dict1[i] = 1
   return dict1, dict1.keys()

list1 = [1, 2, 3, 2, 1, 1, 1, 2, 3, 3, 3, 3]

result = count_elements(list1)
print(result)
# Начало вычисления...
# ({1: 4, 2: 3, 3: 5}, dict_keys([1, 2, 3]))

result = count_elements(True)
print(result)
# Недопустимый тип переданного аргумента
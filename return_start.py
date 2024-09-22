def count_elements(input_list):
  dict1 = {}
  for i in input_list:
      if i in dict1:
          dict1[i] += 1
      else:
          dict1[i] = 1
  return dict1
  return dict1.keys()

list1 = [1, 2, 3, 2, 1, 1, 1, 2, 3, 3, 3, 3]

result = count_elements(list1)
print(result)
# {1: 4, 2: 3, 3: 5}

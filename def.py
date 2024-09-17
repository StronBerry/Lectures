def counter(lst):
  dct = {}
  for i in lst:
    if i in dct:
      dct[i] += 1
    else:
      dct[i] = 1
  print(dct)


list1 = [1, 2, 3, 2, 1, 1, 1, 2, 3, 3, 3, 3]
counter(list1)


list2 = [4, 5, 6, 4, 5, 5, 5, 6, 4, 4, 4, 6]
counter(list2)
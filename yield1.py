def generate_test_data(n):
   for i in range(n):
       yield f"test_data_{i}"
test_data = generate_test_data(10)
print(test_data, type(test_data))
# <generator object generate_test_data at 0x000002299B216E40> <class 'generator'>

# Через NEXT
# test_data = generate_test_data(10)
# print(next(test_data))
# # test_data_0
# print(next(test_data))
# # test_data_1
# # И так далее, пока не закончатся элементы...

# Через FOR

for test in generate_test_data(10):
    print(test)

# test_data_0
# test_data_1
# test_data_2
# ...
# test_data_9
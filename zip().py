# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 90, 88]
#
#
# paired = zip(names, scores)
#
#
# print(list(paired))
# # [('Alice', 85), ('Bob', 90), ('Charlie', 88)]

# expected = [200, 404, 500]
# actual = [200, 404, 500.05]
#
#
# for e, a in zip(expected, actual):
#    if e != a:
#        print(f"Expected {e}, but got {a}")
# # Expected 500, but got 500.05

# headers = ["name", "age", "gender", "pic"]
# row = ["Alice", 28, "Female", "N/E"]
#
#
# user_data = dict(zip(headers, row))
# print(user_data)
# # {'name': 'Alice', 'age': 28, 'gender': 'Female'}

# keys = ["name", "age"]
# values = ["Alice", 30]
# data = dict(zip(keys, values))
# print(data)
# #{'name': 'Alice', 'age': 30}
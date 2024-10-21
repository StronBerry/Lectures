# f = lambda x, y: x**y
# print(f(2, 5))
# # 32
#
funcs = [lambda *args : sum(args) / len(args), lambda x, y : x**y]
print(funcs[0](15, 30, 24))
print(funcs[1](2, 8))
# 23.0
# 256
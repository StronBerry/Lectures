# x = 0
# print('Global x: {}'.format(x))
#
#
# def outer_function():
#     x = 1
#     print('Outer x: {}'.format(x))
#
#     def inner_function():
#         x = 2
#         print('Inner x: {}'.format(x))
#
#     inner_function()
#     print('Outer x: {}'.format(x))
#
#
# outer_function()
# # Global x: 0
# # Inner x: 2
# # Outer x: 1

x = 0
print('Global x: {}'.format(x))


def outer_function():
	x = 1

	def inner_function():
    	    nonlocal x
    	    x = 2
    	    print('Inner x: {}'.format(x))

	inner_function()
	print('Outer x: {}'.format(x))


outer_function()
# Global x: 0
# Inner x: 2
# Outer x: 2
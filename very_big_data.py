very_big_data = (n for n in range(1000000000000))
for n in very_big_data:
    print(n, end=' ')
    if n == 10:
        break

# 0 1 2 3 4 5 6 7 8 9 10

very_big_data = (n for n in range(10000))
very_big_data = list(very_big_data)
print(type(very_big_data), len(very_big_data))
# <class 'list'> 10000
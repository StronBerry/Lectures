def sort_strings_by_last_char(strings):
    return sorted(strings, key=lambda s: s[-1])

strings = ["apple", "banana", "cherry", "date", "elderberry"]
print(sort_strings_by_last_char(strings))
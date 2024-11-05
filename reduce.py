# test_results = [True, True, False, True, True]
#
# all_passed = True
# for result in test_results:
#     all_passed = all_passed and result
#
# print(all_passed)
# # False

# from functools import reduce
#
# test_results = [True, True, False, True, True]
#
# all_passed = reduce(lambda a, b: a and b, test_results)
#
# print(all_passed)
# # False

# test_results = [True, True, False, True, True]
#
# all_passed = all(test_results)
#
# print(all_passed)
# # False

test_cases = [
    {'name': 'Test 1', 'passed': True, 'time': 1.0},
    {'name': 'Test 2', 'passed': False, 'time': 0.5},
    {'name': 'Test 3', 'passed': True, 'time': 1.5}
]
from functools import reduce

summary = reduce(
    lambda acc, test: {
        'total_time': acc['total_time'] + test['time'],
        'passed': acc['passed'] + (1 if test['passed'] else 0),
        'failed': acc['failed'] + (0 if test['passed'] else 1),
    },
    test_cases,
    {'total_time': 0.0, 'passed': 0, 'failed': 0}
)

print(summary)
# {'total_time': 3.0, 'passed': 2, 'failed': 1}

# Без reduce()
# summary = {'total_time': 0.0, 'passed': 0, 'failed': 0}
#
# for test in test_cases:
#     summary['total_time'] += test['time']
#     if test['passed']:
#         summary['passed'] += 1
#     else:
#         summary['failed'] += 1
#
# print(summary)
# # Outputs: {'total_time': 3.0, 'passed': 2, 'failed': 1}
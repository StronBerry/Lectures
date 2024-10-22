test_results = [
   {'name': 'test1', 'status': 'fail', 'time': 2.5},
   {'name': 'test2', 'status': 'pass', 'time': 1.1},
   {'name': 'test3', 'status': 'fail', 'time': 3.1},
   {'name': 'test4', 'status': 'pass', 'time': 0.9}
]

for result in test_results:
   result['status'] = (lambda x: x == 'pass')(result['status'])


for test in test_results:
   print(test)
# {'name': 'test1', 'status': False, 'time': 2.5}
# {'name': 'test2', 'status': True, 'time': 1.1}
# {'name': 'test3', 'status': False, 'time': 3.1}
# {'name': 'test4', 'status': True, 'time': 0.9}
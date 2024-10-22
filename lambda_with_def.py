test_reports = [
   {'name': 'test1', 'status': 'fail', 'time': 2.5, 'details': {'error': 'NullPointerException', 'attempt': 1}},
   {'name': 'test2', 'status': 'pass', 'time': 1.1, 'details': {'attempt': 1}},
   {'name': 'test3', 'status': 'fail', 'time': 3.1, 'details': {'error': 'AssertionError', 'attempt': 2}},
   {'name': 'test4', 'status': 'pass', 'time': 0.9, 'details': {'attempt': 1}}
]
def extract_data(reports, extraction_func):
   return [extraction_func(report) for report in reports]
execution_times = extract_data(test_reports, lambda x: x['time'])
print(execution_times)
# [2.5, 1.1, 3.1, 0.9]
attempt_counts = extract_data(test_reports, lambda x: x['details']['attempt'])
print(attempt_counts)
# [1, 1, 2, 1]
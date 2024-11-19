# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

flights = [
    {"flight_number": 101, "departure": "New York", "destination": "Los Angeles"},
    {"flight_number": 205, "departure": "London", "destination": "Paris"},
    {"flight_number": 312, "departure": "Tokyo", "destination": "Sydney"},
    {"flight_number": 417, "departure": "Dubai", "destination": "New York"},
    {"flight_number": 524, "departure": "Paris", "destination": "Rome"},
    {"flight_number": 633, "departure": "Los Angeles", "destination": "Tokyo"}
]
def find_flight(flights, target_flight_number):
    left, right = 0, len(flights) - 1
    while left <= right:
        mid = (left + right) // 2
        if flights[mid]["flight_number"] == target_flight_number:
            return mid
        elif flights[mid]["flight_number"] < target_flight_number:
            left = mid + 1
        else:
            right = mid - 1
    return -1


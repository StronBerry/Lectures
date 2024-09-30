people = [
   {'name': 'Анна', 'age': 20},
   {'name': 'Борис', 'age': 25},
   {'name': 'Виктор', 'age': 19}
]


def get_age(person):
   return person['age']


sorted_people = sorted(people, key=get_age)
print(sorted_people)
# [{'name': 'Виктор', 'age': 19}, {'name': 'Анна', 'age': 20}, {'name': 'Борис', 'age': 25}]

sorted_people = sorted(people, key=lambda person: person['age'])
print(sorted_people)
# [{'name': 'Виктор', 'age': 19}, {'name': 'Анна', 'age': 20}, {'name': 'Борис', 'age': 25}]
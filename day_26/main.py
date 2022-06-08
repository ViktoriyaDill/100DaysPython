# list_of_numbers = [1, 2, 3]
# new_list = [n + 1 for n in list_of_numbers]
# print(new_list)

# name = "Ivan"
# name_list = [letter for letter in name]
# print(name_list)

# print([num * 2 for num in range(1, 5)])

import random

names = ["Nikita", "Ivan", "Viktoriya", "Alica", "Stefaniya"]
# print([n.upper() for n in names if len(n) > 5])
students_score = {student: random.randint(45, 100) for student in names}
print(students_score.items())
passed_student = {name: mark for (name, mark) in students_score.items() if students_score[name] > 65}
print(passed_student)

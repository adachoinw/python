names = ["Alex", "Caroline", " Beth", "Dave", "Eleanor", "Freddie"]
cap_names = [name.upper() for name in names if len(name) > 5]
print(cap_names)


# with open("file1.txt") as file1:
#     f1_list = file1.readlines()
#
# with open("file2.txt") as file2:
#     f2_list = file2.readlines()
#
# result = [int(num) for num in f1_list if num in f2_list]
# # # Write your code above 👆
#
# print(result)


import random
students_scores = {student:random.randint(1, 100) for student in names}
# passed_students = {new_key:new_value for (key, value) in dictionary.items()}
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)
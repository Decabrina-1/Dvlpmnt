import random

student_list = []

try:
    with open("list_of_students.txt", "r", encoding="utf-8") as file:
        for line in file:
            student_list.append(line.strip())
except FileNotFoundError:
    print("Файл не найден")
    exit()

if len(student_list) < 5:
    print("В файле меньше 5 студентов.")
else:
    selected_students = []
    while len(selected_students) < 5:
        x = random.choice(student_list)
        if x not in selected_students:
            selected_students.append(x)

    print("Список выбранных студентов:")
    for student in selected_students:
        print(student)
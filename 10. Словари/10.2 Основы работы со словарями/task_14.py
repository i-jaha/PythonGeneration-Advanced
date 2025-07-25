'''Информация об учебных курсах 🎓
Напишите программу, которая по номеру курса выводит информацию о данном курсе.
    | Номер курса (ключ) | Номер аудитории (значение) | Преподаватель (значение) | Время (значение) |
    | ------------------ | -------------------------- | ------------------------ | ---------------- |
    | CS101              | 3004                       | Хайнс                    | 8:00             |
    | CS102              | 4501                       | Альварадо                | 9:00             |
    | CS103              | 6755                       | Рич                      | 10:00            |
    | NT110              | 1244                       | Берк                     | 11:00            |
    | CM241              | 1411                       | Ли                       | 13:00            |

На вход программе подается одна строка – номер курса.

Программа должна вывести 
номер курса, 
затем номер аудитории, 
имя преподавателя 
и время проведения курса 
в соответствии с примерами.

Примечание 1. 
Используйте словарь вместо условного оператора.

Примечание 2. 
Для удобного вывода используйте строковый метод format() или f-строки.
'''

courses = {
    "CS101": ["3004",   "Хайнс",        "8:00"],
    "CS102": ["4501",   "Альварадо",    "9:00"],
    "CS103": ["6755",   "Рич",          "10:00"],
    "NT110": ["1244",   "Берк",         "11:00"],
    "CM241": ["1411",   "Ли",           "13:00"]
}
course = input()
if course in courses:
    room, teacher, time = courses[course]
    print(f"{course}: {room}, {teacher}, {time}")
else: 
    print("Course not found.")
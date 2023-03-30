"""
2. Деканат.
Дано: n - целое число.

Задание: спроектируйте следующую предметную область, используя объектно-ориентированный подход.

Сотрудники деканата каждый семестр решают проблему формирования отчетных ведомостей студентов,
разных групп и курсов. Цель - получить информацию о среднем балле каждого студента, группы,
а также предмета(например, средний балл по физкультуре в группе 433 составляет 4.1).
Такая информация поможет сформировать список студентов, которых нужно отчислить и стипендиатов,
а также наиболее "проблемные" предметы.
"""
import random
from Tasks_12.Task_2_updated.Classes.Relations.student_subject_in_group import Student_Subject
from Tasks_12.Task_2_updated.Classes.Relations.group_subject import Group_Subject

# Исходные данные
faculties = ["ФВС"]
groups = ["322", "580-3"]
subjects = ["Физика", "ООП", "БД", "ИИ"]
persons = ["Гена", "Рима", "Витя", "Маша"]

persons_len = len(persons)
half_persons_len = persons_len / 2

# Создание экземпляров классов
for person, n in zip(persons, range(persons_len)):
    for subject in subjects:
        if n < half_persons_len:
            Student_Subject(faculties[0], groups[0], person, subject, mark=random.randint(2, 5))
        else:
            Student_Subject(faculties[0], groups[1], person, subject, mark=random.randint(2, 5))


if __name__ == '__main__':
    print("Выведем список студентов и их оценок: ")
    for student in Student_Subject.get_relations().values():
        print(student)

    print("\nВыведем список групп и их предметов: ")
    for subject_ in Group_Subject.get_relations().values():
        print(subject_)

    print("\nВыведем список средних оценок по каждому предмету: ")
    for subject_mark in Student_Subject.calculate_avg_mark_each_subject():
        print(subject_mark)

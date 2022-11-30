"""
3. Деканат.
Дано: список студентов: каждый элемент списка содержит фамилию, имя, отчество,
год рождения, курс, номер группы, оценки по пяти предметам.

Задание: реализуйте сл. функции:

1) возвращает список студентов по курсу, причем студенты одного курса
располагались в алфавитном порядке;
2) находит средний балл каждой группы по каждому предмету;
3) определяет самого старшего студента и самого младшего студента.
4) возвращает словарь, где для каждой группы определен лучший с точки
зрения успеваемости студент.
"""
import sys


class StudentDataAnalyzer:
    def __init__(self, students):
        self.students = students

    def get_sorted_students_list(self):
        """
        Функция, которая сортирует список студентов определенного курса.
        :return: Список -> студенты определенного курса, отсортированные
        по фамилии, в алфавитном порядке.
        """
        course = set_int_value()
        array = self.students
        students_of_course = [i for i in array if i[4] == course]

        return sorted(students_of_course, key=lambda x: x[0])

        # Также есть другой способ:
        # >>> from operator import itemgetter
        # >>> return sorted(students_of_course, key=itemgetter(0))

    def get_every_group_average_mark_each_subject(self):
        """
        Функция, которая считает среднюю оценку по каждому предмету
        каждой группы.
        :return: Словарь -> группа: список средних оценок.
        """
        array = self.students
        group_index = 5
        marks_start_index = 6
        each_group = {}  # Словарь: группа-оценки.

        for i in array:
            group = i[group_index]
            marks = i[marks_start_index:]

            if group in each_group.keys():
                # Использую 'lambda', чтобы сложить между собой
                # текущие оценки и оценки нового студента.
                sum_of_marks = list(map(lambda x, y: x + y,
                                        marks, each_group[group][0]))
                students_amount = each_group[group][1]
                each_group[group] = [sum_of_marks, students_amount + 1]
            else:
                each_group[group] = [marks, 1]

        for i, j in each_group.items():
            # Делим каждую оценку на количество студентов.
            j = list(map(lambda x, y=j[1]: x / y, j[0]))
            each_group[i] = j

        return each_group

    def get_oldest_youngest_student(self):
        """
        Функция, которая определяет самого молодого и старшего студента.
        :return: Кортеж списков.
        """
        array = self.students
        burn_year_index = 3
        student_full_name_end_index = 3
        # Значения по умолчанию
        oldest = youngest = [array[0][:student_full_name_end_index],
                             array[0][burn_year_index]]

        for i in array:
            burn_year = i[burn_year_index]

            if burn_year < youngest[1]:
                youngest = [i[:student_full_name_end_index], i[burn_year_index]]
            elif burn_year > oldest[1]:
                oldest = [i[:student_full_name_end_index], i[burn_year_index]]

        return oldest, youngest

    def get_best_student_each_group(self):
        """
        Функция, определяющая лучшего студента в каждой группе.
        :return: Словарь -> группа-лучший ученик.
        """
        array = self.students
        group_index = 5
        marks_start_index = 6
        student_full_name_end_index = 3
        each_group = {}  # Словарь: группа-лучший ученик.

        for i in array:
            group = i[group_index]
            marks = i[marks_start_index:]
            student = i[:student_full_name_end_index]

            if group in each_group.keys():
                if sum(each_group[group][1]) < sum(marks):
                    each_group[group] = [student, marks]
            else:
                each_group[group] = [student, marks]

        return each_group


def set_int_value():
    """
    Функция ввода и проверки чисел.
    :return: Натуральное число.
    """
    while 1:
        try:
            x = input('Введите число: ')
            int_x = int(x)

            if not 1 <= int_x <= 5:
                raise Exception

            return int_x

        except ValueError:
            print('Ошибка. Вы можете ввести только натуральное число!')

        except Exception:
            print('Ошибка. Число должно быть в диапазоне [1; 5]!')


students = [
        ['Звезда', 'Патрик', 'Абрамович', 2021, 3, '580-3', 5, 5, 5, 5, 5],
        ['Живой', 'Огурец', 'Александрович', 1991, 2, '741', 1, 2, 3, 4, 1],
        ['Горюнов', 'Аркадий', 'Сергеевич', 2002, 3, '580-3', 5, 4, 5, 5, 4],
        ['Маск', 'Илона', 'Шмидт', 2005, 2, '741', 5, 5, 5, 5, 5],
        ['Мракомысл', 'Олег', 'Батькович', 1999, 4, '39', 2, 2, 2, 2, 4],
]

students_of_tusur = StudentDataAnalyzer(students)

while 1:
    print('Выберите действие:\n'
          '1) Найти лучшего студента на курсе;\n'
          '2) Найти средний балл по каждому предмету каждой группы;\n'
          '3) Найти самого молодого и старшего ученика;\n'
          '4) Найти лучшего студента в каждой группе;\n'
          '5) Выход.')
    choice = set_int_value()

    match choice:
        case 1:
            print('Вас интересуют студенты курса: ')
            print(students_of_tusur.get_sorted_students_list())
        case 2:
            print(students_of_tusur.
                  get_every_group_average_mark_each_subject())
        case 3:
            print(students_of_tusur.get_oldest_youngest_student())
        case 4:
            print(students_of_tusur.get_best_student_each_group())
        case 5:
            sys.exit()


from Tasks_12.Task_2_updated.Classes.Relations.group_student import Group_Person
from Tasks_12.Task_2_updated.Classes.Relations.group_subject import Group_Subject


# Выбрано такое написание имен, чтобы показать связь М:М.
class Student_Subject(Group_Person, Group_Subject):
    id = 0
    relations = dict()

    def __init__(self, faculty_name, group_name, person_name, subject_name, mark):
        Group_Person.__init__(self, faculty_name, group_name, person_name)
        Group_Subject.__init__(self, faculty_name, group_name, subject_name)
        self.mark = mark

        Student_Subject.id += 1
        Student_Subject.relations[Student_Subject.id] = [
            super().get_faculty_name(),
            super().get_group_name(),
            super().get_person_name(),
            super().get_subject_name(),
            self.mark
        ]

    def __repr__(self):
        return repr(self.relations)

    @classmethod
    def get_relations(cls):
        return cls.relations

    @classmethod
    def calculate_avg_mark_each_subject(cls):
        summary_marks = dict()

        faculty_index = 0
        group_index = 1
        person_index = 2
        subject_index = 3
        mark_index = 4

        students_amount_index = 0
        summary_mark_index = 1

        for student in cls.relations.values():
            title = " ".join([
                student[group_index],
                student[subject_index],
            ])

            if title not in summary_marks.keys():
                students_amount = 1
                summary_mark = student[mark_index]
                summary_marks[title] = [students_amount, summary_mark]
            else:
                summary_marks[title][students_amount_index] += 1
                summary_marks[title][summary_mark_index] += student[mark_index]

        avg_marks = [
            {
                key: value[summary_mark_index] / value[students_amount_index]
            }
            for key, value in summary_marks.items()
        ]

        return avg_marks


if __name__ == '__main__':
    pass

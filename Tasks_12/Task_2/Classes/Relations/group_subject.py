from Tasks_12.Task_2.Classes.University.group import Group
from Tasks_12.Task_2.Classes.University.subject import Subject


# Выбрано такое написание имен, чтобы показать связь М:М.
class Group_Subject(Group, Subject):
    id = 0
    relations = {}

    def __init__(self, faculty_name, group_name, subject_name):
        Group.__init__(self, faculty_name, group_name)
        Subject.__init__(self, subject_name)

        new_relation = [
            super().get_faculty_name(),
            super().get_group_name(),
            super().get_subject_name(),
        ]

        if new_relation not in Group_Subject.relations.values():
            Group_Subject.id += 1
            Group_Subject.relations[Group_Subject.id] = new_relation

    def __repr__(self):
        return repr(self.relations)


    @classmethod
    def get_relations(cls):
        return cls.relations


if __name__ == '__main__':
    pass

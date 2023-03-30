from Tasks_12.Task_2_updated.Classes.University.group import Group
from Tasks_12.Task_2_updated.Classes.person import Person


# Выбрано такое написание имен, чтобы показать связь М:М.
class Group_Person(Group, Person):
    id = 0
    relations = {}

    def __init__(self, faculty_name, group_name, person_name):
        Group.__init__(self, faculty_name, group_name)
        Person.__init__(self, person_name)

        new_relation = [
            super().get_faculty_name(),
            super().get_group_name(),
            super().get_person_name(),
        ]

        if new_relation not in Group_Person.relations.values():
            Group_Person.id += 1
            Group_Person.relations[Group_Person.id] = new_relation



    def __repr__(self):
        return repr(self.relations)

    @classmethod
    def get_relations(cls):
        return cls.relations

if __name__ == '__main__':
    pass

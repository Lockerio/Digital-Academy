from Tasks_12.Task_2.Classes.University.faculty import Faculty


class Group(Faculty):
    def __init__(self, faculty_name, group_name):
        super().__init__(faculty_name)
        self.group_name = group_name

    def __repr__(self):
        return repr(self.group_name)

    def get_group_name(self):
        return self.group_name


if __name__ == '__main__':
    pass

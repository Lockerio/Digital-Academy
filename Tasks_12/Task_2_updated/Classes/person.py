class Person:
    def __init__(self, person_name):
        self.person_name = person_name

    def __repr__(self):
        return repr(self.person_name)

    def get_person_name(self):
        return self.person_name


if __name__ == '__main__':
    pass

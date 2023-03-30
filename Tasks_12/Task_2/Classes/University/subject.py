class Subject:
    def __init__(self, subject_name):
        self.subject_name = subject_name

    def __repr__(self):
        return repr(self.subject_name)

    def get_subject_name(self):
        return self.subject_name


if __name__ == '__main__':
    pass

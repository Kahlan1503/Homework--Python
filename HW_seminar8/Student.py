class Student:

    def __init__(self, name, surname, group, subjects=None):
        self.name = name
        self.group = group
        self.surname = surname
        self.subjects = {} if subjects is None else subjects

    def __str__(self):
        return f"{self.surname}, {self.name}, {self.group}, {self.subjects}"

    def add_score(self, subject, score):
        self.subjects[subject] = self.subjects.get(subject, []) + [score]

    @classmethod
    def load(cls, json_data):
        return cls(**json_data)

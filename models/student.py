from models.subject import Subject


class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def get_subject(self, title):
        for subject in self.subjects:
            if subject.title == title:
                return subject
        return None

    def to_dict(self):
        return {
            "name": self.name,
            "subjects": [
                subject.to_dict()
                for subject in self.subjects
            ]
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(data["name"])

        for subject_data in data.get("subjects", []):
            student.add_subject(
                Subject.from_dict(subject_data)
            )

        return student
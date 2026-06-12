from models.assignment import Assignment


class Subject:
    def __init__(self, title):
        self.title = title
        self.assignments = []

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def get_assignment(self, title):
        for assignment in self.assignments:
            if assignment.title == title:
                return assignment
        return None

    def to_dict(self):
        return {
            "title": self.title,
            "assignments": [
                assignment.to_dict()
                for assignment in self.assignments
            ]
        }

    @classmethod
    def from_dict(cls, data):
        subject = cls(data["title"])

        for assignment_data in data.get("assignments", []):
            subject.add_assignment(
                Assignment.from_dict(assignment_data)
            )

        return subject
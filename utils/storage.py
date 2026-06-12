import json
from models.student import Student

DATABASE_FILE = "data/database.json"


def save_students(students):
    data = [student.to_dict() for student in students]

    with open(DATABASE_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_students():
    try:
        with open(DATABASE_FILE, "r") as file:
            data = json.load(file)

        return [
            Student.from_dict(student_data)
            for student_data in data
        ]

    except (FileNotFoundError, json.JSONDecodeError):
        return []
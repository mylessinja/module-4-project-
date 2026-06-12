import argparse

from models.student import Student
from models.subject import Subject
from models.assignment import Assignment
from utils.storage import save_students, load_students

students = load_students()


def add_student(name):
    student = Student(name)
    students.append(student)
    save_students(students)
    print(f"Student '{name}' added successfully!")


def list_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print(f"- {student.name}")


def add_subject(student_name, subject_title):
    for student in students:
        if student.name == student_name:
            student.add_subject(Subject(subject_title))
            save_students(students)
            print(f"Subject '{subject_title}' added to {student_name}")
            return

    print("Student not found.")


def add_assignment(subject_title, assignment_title):
    for student in students:
        subject = student.get_subject(subject_title)

        if subject:
            subject.add_assignment(
                Assignment(assignment_title)
            )
            save_students(students)
            print(f"Assignment '{assignment_title}' added.")
            return

    print("Subject not found.")


def list_assignments(subject_title):
    for student in students:
        subject = student.get_subject(subject_title)

        if subject:
            if not subject.assignments:
                print("No assignments found.")
                return

            for assignment in subject.assignments:
                status = "✅" if assignment.completed else "❌"
                print(f"{status} {assignment.title}")
            return

    print("Subject not found.")


def complete_assignment(subject_title, assignment_title):
    for student in students:
        subject = student.get_subject(subject_title)

        if subject:
            assignment = subject.get_assignment(
                assignment_title
            )

            if assignment:
                assignment.mark_complete()
                save_students(students)
                print("Assignment completed!")
                return

    print("Assignment not found.")


parser = argparse.ArgumentParser(
    description="Student Assignment Tracker"
)

subparsers = parser.add_subparsers(dest="command")

# student
student_parser = subparsers.add_parser("student")
student_parser.add_argument("--name", required=True)

# students
subparsers.add_parser("students")

# subject
subject_parser = subparsers.add_parser("subject")
subject_parser.add_argument("--student", required=True)
subject_parser.add_argument("--title", required=True)

# assignment
assignment_parser = subparsers.add_parser("assignment")
assignment_parser.add_argument("--subject", required=True)
assignment_parser.add_argument("--title", required=True)

# assignments
list_assignment_parser = subparsers.add_parser(
    "assignments"
)
list_assignment_parser.add_argument(
    "--subject",
    required=True
)

# complete
complete_parser = subparsers.add_parser(
    "complete"
)
complete_parser.add_argument(
    "--subject",
    required=True
)
complete_parser.add_argument(
    "--title",
    required=True
)

args = parser.parse_args()

if args.command == "student":
    add_student(args.name)

elif args.command == "students":
    list_students()

elif args.command == "subject":
    add_subject(args.student, args.title)

elif args.command == "assignment":
    add_assignment(args.subject, args.title)

elif args.command == "assignments":
    list_assignments(args.subject)

elif args.command == "complete":
    complete_assignment(
        args.subject,
        args.title
    )

else:
    parser.print_help()

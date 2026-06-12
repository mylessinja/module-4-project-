import argparse
import os
import json

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "database.json")

def load_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    if not os.path.exists(DB_PATH):
        with open(DB_PATH, "w") as f:
            json.dump({"students": []}, f, indent=2)
    with open(DB_PATH) as f:
        return json.load(f)

def save_db(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=2)

def find_student(data, name):
    for s in data["students"]:
        if s["name"].lower() == name.lower():
            return s
    return None

def find_subject(student, title):
    for s in student["subjects"]:
        if s["title"].lower() == title.lower():
            return s
    return None

def cmd_add_student(args):
    data = load_db()
    if find_student(data, args.name):
        print("Student already exists.")
        return
    data["students"].append({"name": args.name, "subjects": []})
    save_db(data)
    print("Student added successfully!")

def cmd_list_students(args):
    data = load_db()
    if not data["students"]:
        print("No students found.")
        return
    for s in data["students"]:
        print(f"  - {s['name']} ({len(s['subjects'])} subjects)")

def cmd_add_subject(args):
    data = load_db()
    student = find_student(data, args.student)
    if not student:
        print("Student not found.")
        return
    student["subjects"].append({"title": args.title, "assignments": []})
    save_db(data)
    print("Subject added!")

def cmd_list_subjects(args):
    data = load_db()
    student = find_student(data, args.student)
    if not student:
        print("Student not found.")
        return
    for s in student["subjects"]:
        print(f"  - {s['title']}")

def cmd_add_assignment(args):
    data = load_db()
    student = find_student(data, args.student)
    if not student:
        print("Student not found.")
        return
    subject = find_subject(student, args.subject)
    if not subject:
        print("Subject not found.")
        return
    subject["assignments"].append({"title": args.title, "due_date": args.due_date, "completed": False})
    save_db(data)
    print("Assignment added!")

def cmd_list_assignments(args):
    data = load_db()
    student = find_student(data, args.student)
    if not student:
        print("Student not found.")
        return
    subject = find_subject(student, args.subject)
    if not subject:
        print("Subject not found.")
        return
    for a in subject["assignments"]:
        status = "Done" if a["completed"] else "Pending"
        print(f"  [{status}] {a['title']}")

def cmd_complete(args):
    data = load_db()
    student = find_student(data, args.student)
    if not student:
        print("Student not found.")
        return
    subject = find_subject(student, args.subject)
    if not subject:
        print("Subject not found.")
        return
    for a in subject["assignments"]:
        if a["title"].lower() == args.title.lower():
            a["completed"] = True
            save_db(data)
            print("Assignment marked as complete!")
            return
    print("Assignment not found.")

def main():
    parser = argparse.ArgumentParser(description="Student Assignment Tracker")
    sub = parser.add_subparsers(dest="command")
    p = sub.add_parser("add-student")
    p.add_argument("--name", required=True)
    sub.add_parser("list-students")
    p = sub.add_parser("add-subject")
    p.add_argument("--student", required=True)
    p.add_argument("--title", required=True)
    p = sub.add_parser("list-subjects")
    p.add_argument("--student", required=True)
    p = sub.add_parser("add-assignment")
    p.add_argument("--student", required=True)
    p.add_argument("--subject", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--due-date", default="")
    p = sub.add_parser("list-assignments")
    p.add_argument("--student", required=True)
    p.add_argument("--subject", required=True)
    p = sub.add_parser("complete-assignment")
    p.add_argument("--student", required=True)
    p.add_argument("--subject", required=True)
    p.add_argument("--title", required=True)
    args = parser.parse_args()
    commands = {
        "add-student": cmd_add_student,
        "list-students": cmd_list_students,
        "add-subject": cmd_add_subject,
        "list-subjects": cmd_list_subjects,
        "add-assignment": cmd_add_assignment,
        "list-assignments": cmd_list_assignments,
        "complete-assignment": cmd_complete,
    }
    if args.command in commands:
        commands[args.command](args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

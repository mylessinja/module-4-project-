Student Assignment Tracker CLI

A Python-based Command Line Interface (CLI) application that helps students manage their subjects and assignments. The application allows users to create students, add subjects, assign coursework, track assignment completion, and store all data permanently using JSON file storage.

This project demonstrates Object-Oriented Programming (OOP), file persistence, command-line argument parsing, modular programming, and version control using Git and GitHub.

Project Overview

Managing assignments manually can become difficult when a student is enrolled in multiple subjects. The Student Assignment Tracker CLI provides a simple way to organize subjects and assignments directly from the terminal.

Users can:

Create student profiles
Add subjects to students
Create assignments for subjects
View assignments
Mark assignments as completed
Save and load data automatically using JSON
Features
Student Management
Add new students
View all students in the system
Subject Management
Add subjects to a student
Associate multiple subjects with one student
Assignment Management
Add assignments to a subject
View assignments by subject
Mark assignments as completed
Track assignment status
Data Persistence
Store data in JSON format
Automatically load saved data when the application starts
Preserve information between sessions
Command Line Interface
User-friendly terminal commands
Built with Python's argparse module
Includes help documentation for commands
Technologies Used
Python 3.12
Object-Oriented Programming (OOP)
argparse
JSON
Git
GitHub
Virtual Environment (venv)
Rich (PyPI package)
Pytest
Project Structure
student-assignment-tracker/
│
├── data/
│   └── database.json
│
├── models/
│   ├── student.py
│   ├── subject.py
│   └── assignment.py
│
├── utils/
│   └── storage.py
│
├── tests/
│   └── test_assignment.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
Object-Oriented Design

The project uses three primary classes:

Student

Represents a student.

Attributes:

name
subjects

Methods:

add_subject()
get_subject()
to_dict()
from_dict()
Subject

Represents a subject belonging to a student.

Attributes:

title
assignments

Methods:

add_assignment()
get_assignment()
to_dict()
from_dict()
Assignment

Represents a student's assignment.

Attributes:

title
due_date
completed

Methods:

mark_complete()
to_dict()
from_dict()
Installation
Clone Repository
git clone https://github.com/YOUR_USERNAME/student-assignment-tracker.git
Enter Project Folder
cd student-assignment-tracker
Create Virtual Environment
python3 -m venv venv
Activate Virtual Environment

Linux/Mac:

source venv/bin/activate

Windows:

venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Usage
Display Help
python3 main.py -h
Add a Student
python3 main.py student --name "Victor"

Output:

Student 'Victor' added successfully!
View Students
python3 main.py students

Output:

- Victor
- John
Add a Subject
python3 main.py subject --student "Victor" --title "Python"

Output:

Subject 'Python' added to Victor
Add an Assignment
python3 main.py assignment --subject "Python" --title "OOP Lab"

Output:

Assignment 'OOP Lab' added.
View Assignments
python3 main.py assignments --subject "Python"

Output:

❌ OOP Lab
Complete an Assignment
python3 main.py complete --subject "Python" --title "OOP Lab"

Output:

Assignment completed!
Verify Completion
python3 main.py assignments --subject "Python"

Output:

✅ OOP Lab
Data Storage

All application data is stored in:

data/database.json

Example:

{
    "students": [
        {
            "name": "Victor",
            "subjects": [
                {
                    "title": "Python",
                    "assignments": [
                        {
                            "title": "OOP Lab",
                            "due_date": "",
                            "completed": true
                        }
                    ]
                }
            ]
        }
    ]
}
Testing

Run tests using Pytest:

pytest

Example:

pytest tests/
Future Improvements

Potential enhancements include:

Delete students
Delete subjects
Delete assignments
Assignment deadlines
Search functionality
Assignment priority levels
Rich terminal tables
Interactive menu system
Export data to CSV
Learning Outcomes

This project demonstrates:

Object-Oriented Programming
Class Relationships
File Handling
JSON Serialization
Command-Line Interfaces
Python Modules
Package Management
Software Testing
Git Version Control
GitHub Collaboration
Author

Victor Sinja Wamwoyo

Module 4 Final Project

Moringa School

License

This project is intended for educational purposes and learning Python software development concepts.

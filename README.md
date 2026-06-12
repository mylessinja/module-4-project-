# Student Assignment Tracker CLI

## Overview

Student Assignment Tracker CLI is a Python-based command-line application that helps students organize and manage their coursework. The application allows users to create students, add subjects, manage assignments, and track assignment completion status. All data is stored locally using JSON for persistence.

---

## Features

* Add and manage students
* Add subjects to students
* Add assignments to subjects
* View all students
* View assignments for a subject
* Mark assignments as completed
* Save and load data using JSON
* Command-line interface using argparse
* Object-Oriented Programming (OOP) design

---

## Project Structure

```text
student-assignment-tracker/
│
├── main.py
│
├── models/
│   ├── student.py
│   ├── subject.py
│   └── assignment.py
│
├── utils/
│   └── storage.py
│
├── data/
│   └── database.json
│
├── tests/
│   └── test_assignment.py
│
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python 3.12
* argparse
* JSON
* pytest
* rich

---

## Installation

### Clone the Repository

```bash
git clone <your-github-repository-url>
cd student-assignment-tracker
```

### Create a Virtual Environment

```bash
python3 -m venv venv
```

### Activate the Virtual Environment

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Add a Student

```bash
python3 main.py add-student --name "Victor"
```

### List Students

```bash
python3 main.py list-students
```

### Add a Subject

```bash
python3 main.py add-subject --student "Victor" --title "Python"
```

### Add an Assignment

```bash
python3 main.py add-assignment --subject "Python" --title "OOP Lab"
```

### View Assignments

```bash
python3 main.py list-assignments --subject "Python"
```

### Mark an Assignment as Complete

```bash
python3 main.py complete-assignment --subject "Python" --title "OOP Lab"
```

---

## Object-Oriented Design

The application uses three main classes:

### Student

Represents a student and contains multiple subjects.

### Subject

Represents a course or subject and contains multiple assignments.

### Assignment

Represents an individual assignment and tracks its completion status.

Relationship Structure:

```text
Student
 └── Subject
      └── Assignment
```

---

## Data Persistence

Project data is stored in:

```text
data/database.json
```

This allows information to remain available even after the application is closed.

---

## Testing

Run tests using:

```bash
pytest
```

---

## Future Improvements

* Delete assignments
* Edit assignment titles
* Add due dates
* Search assignments
* Display output using Rich tables
* Add subject listing command

---

## Author

Victor Sinja

Moringa School – Module 4 Final Project

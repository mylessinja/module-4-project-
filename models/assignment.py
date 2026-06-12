class Assignment:
    def __init__(self, title, due_date="", completed=False):
        self.title = title
        self.due_date = due_date
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "due_date": self.due_date,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            due_date=data.get("due_date", ""),
            completed=data.get("completed", False)
        )
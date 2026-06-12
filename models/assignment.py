class Assignment:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            completed=data.get("completed", False)
        )
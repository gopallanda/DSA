class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name}: {self.score}"

class Toppers(Student):
    def __init__(self):
        self.top_students = []

    def add_student(self, student):
        self.top_students.append(student)
        # Sort the list by score in descending order and keep only the top 3
        self.top_students = sorted(self.top_students, key=lambda x: x.score, reverse=True)[:3]

    def display_toppers(self):
        print("Top 3 Students:")
        for student in self.top_students:
            print(student)

# Example usage
students = [
    Student("Alice", 90),
    Student("Bob", 85),
    Student("Charlie", 92),
    Student("David", 88),
    Student("Eva", 95),
]

toppers = Toppers()
for student in students:
    toppers.add_student(student)

toppers.display_toppers()

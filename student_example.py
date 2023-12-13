class Course:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Course named {self.name}"
        

    def __str__(self) -> str:
        return f"Course named {self.name} with id {self.id}"
class Student:
    def __init__(self, name: str, id: int, l) -> None:
        self.name = name
        self.id = id
        self.courses = l

    def __str__(self) -> str:
        return f"Student named {self.name} with id {self.id} and courses {self.courses}"
    
if __name__ == "__main__":
    student = Student("John", 123, [Course("Math"), Course("English")])
    print(student)
    o= {
        "name": "John",
        "id": 123,
        "courses": [
            {
                "name": "Math"
            },
            {
                "name": "English"
            }
        ]
    }
    print(o)

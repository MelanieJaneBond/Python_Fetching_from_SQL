from student import Student
from instructor import Instructor

class Exercise(Student, Instructor):
    def __init__(self):
        Student.__init__(self, first_name, last_name)
        Instructor.__init__(self, first_name, last_name)
        self.name = ""
        self.language = ""

    # def cr(self, Student):
    #     Student.exercises.append[self.name]
    #     print(f"The {self.name} exercise was assigned to {}")

    def assign_exercise_to(self, 
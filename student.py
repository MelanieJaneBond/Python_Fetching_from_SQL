from cohort import Cohort

class Student():
    def __init__(self, first_name, last_name):
        self.sr_first_name = first_name
        self.sr_last_name = last_name
        self.slack = ""
        self.exercises = []

#a student is in a cohort
# a student also has a collection of exercises

Melanie = Student("Melanie", "Bond")

print(f"{Melanie.exercises}")
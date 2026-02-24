class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 37.5


jo = WorkingStudent('Jo', 'MIT', 15.5)
print(jo.salary)
jo.marks.append(57)
jo.marks.append(99)
print(jo.average())
print(jo.weekly_salary())


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property # calculates values from the objects property
    def weekly_salary(self):
        return self.salary * 37.5


jo = WorkingStudent('Jo', 'MIT', 15.5)

print(jo.weekly_salary)

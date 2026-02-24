class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student_one = Student('Terry Crews', [70, 88, 90, 99])

print(student_one.name, f"\n{student_one.average()}")


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

    def __repr__(self):  # Code oriented string representing the object
        return f'Garage {self.cars}'

    def __str__(self):  # user oriented string description
        return f'Garage with {len(self)} cars.'


ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')

print(len(ford))
print(ford[0])  # Garage.__getitem__(ford, 0)

for car in ford:  # iterates for loop using 'len' and 'getitem'
    print(car)

print(ford)

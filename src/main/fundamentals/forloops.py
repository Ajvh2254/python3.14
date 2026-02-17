friends = ["Rolf", "Jen", "Anne"]

for friend in friends:
    print(friend)

for index in range(5, 10):
    print(index)

for index in range(2, 21, 3):
    print(index)

students = [
    {"name": "Tuco", "grade": 90},
    {"name": "hector", "grade": 70},
    {"name": "Nacho", "grade": 100},
    {"name": "Don Hector", "grade": 80}
]

for student in students:
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has a grade of {grade}.")

friends = [{"Chester", 10}, {"Timmy", 10}, {"AJ", 10}]

for name, age in friends: # desturcturing: extracts name and age from tuples as the loop iterates
    print(f"{name} is {age} years old")

friend_ages = {"John Stamos": 25, "Anne Franke": 22, "Terry Crews":36}

for age in friend_ages.values(): # grabs age values from list
    print(age)

for name, age in friend_ages.items():
    print(f"{name} is {age} years old")
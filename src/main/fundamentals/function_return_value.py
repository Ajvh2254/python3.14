cars = [
    {"make": "Honda", "model": "Accord", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Honda", "model": "Civic", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Acura", "model": "RSX", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Acura", "model": "NSX", "mileage": 31000, "fuel_consumed": 235}
]

def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg

def car_name(car):
    name = f"{car['make']} {car['model']}"
    return name

def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)

    print(f"{name} does {mpg} miles per gallon")

for car in cars:
    print_car_info(car)

def divide(x, y):
    if y == 0:
        return "You tried to divide by zero"
    else:
        return x / y

divide(10, 2)
divide(6, 0)

def divide(x, y): # this function and the following code return the same answer
    return x / y

divide = lambda x, y: x / y # achieves the same as the above function
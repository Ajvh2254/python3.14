def greet():
    name = input("Enter your name:")
    print(f"Hello, {name}!")


greet()  # have to call the function to run it


def calculate_mpg(car_to_calculate):
    mpg = car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per gallon")

calculate_mpg({
    "make": "Ford",
    "model": "Fiesta",
    "mileage": 23000,
    "fuel_consumed": 460
    })

cars = [
    {"make": "Honda", "model": "Accord", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Honda", "model": "Civic", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Acura", "model": "RSX", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Acura", "model": "NSX", "mileage": 31000, "fuel_consumed": 235}
]

def calculate_mpg(car_to_calculate):
    mpg = car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per gallon")

for car in cars:
    calculate_mpg(car)
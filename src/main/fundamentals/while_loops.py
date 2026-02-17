user_input = input("u wanna run that shit? (yes/no): ")

while user_input == "yes":
    print("We runnin that shit")
    user_input = input("u wanna run that shit? (yes/no): ")

print("we stopped dat shit")

user_input = input("Enter q or p: ")

while user_input != "q":
    if user_input == "p":
        print("Hello")
        user_input = input("Enter q or p: ")
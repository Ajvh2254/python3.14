def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid. Using default value 0.')
        return 0
    else:
        n_square = n ** 2
        return n_square


print(power_of_two())


def interact():
    while True:
        try:
            user_input = int(input('Please input an integer:'))
        except ValueError:
            print('Please input integers only')
        else:
            print('{} is {}. '.format(user_input, 'even' if user_input % 2 == 0 else 'odd'))
        finally:
            user_input = input('Do you want to play again? (y/N):')
        if user_input != 'y':
            print('Goodbye')
            break

print(interact())
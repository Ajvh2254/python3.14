from utils import sql_database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def menu():
    sql_database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown command. Please try again")

        user_input = input(USER_CHOICE)

def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')

    sql_database.add_book(name, author)


def list_books():
    books = sql_database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {'read'}")


def prompt_read_book():
    name = input('Enter the book name you just finished: ')

    sql_database.mark_book_as_read(name)


def prompt_delete_book():
    name = input('Enter the book name you wish to delete: ')

    sql_database.delete_book(name)


menu()
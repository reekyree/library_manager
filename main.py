# A program for managing a personal library of books.



def add_book():
    books = {}

    book = input("Please enter the name of a book: ")

    author = input(f"Who was the auhtor of {book}? ")

    books.update({book : author})

    for key, value in books.items():
        print(f"{key} by {value}")


add_book()
add_book()


# A program for managing a personal library of books.

import pickle

running = True
books = {}

def add_book(books):
    
    book = input("Enter the title: ")

    author = input(f"Enter the author: ")

    books.update({book : author})

def save_books(books):

    if len(books) == 0:
        print("Nothing to save!")


while running:

    print("1. Add a new book")
    print("2. Save booklist")
    print("3. Quit")
    choice = int(input("Enter a command: "))
    if choice == 1:
        add_book(books)
    elif choice == 2:
        save_books(books)
    elif choice == 3:
        running = False

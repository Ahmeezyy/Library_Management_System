from Book_Class import Book
from Library_Class import Library
# User interface used to interact with the library.
def main():
    library = Library()

# Displays options on menu screen.
    while True:
        print("Welcome to the Library Management System!")
        print("-Search for a book (Type search)")
        print("-Add a new book (Type add)")
        print("-Display Books (Type display)")
        print("-Check out (Type check out)")
        print("-Check in (Type check in)")
        print("-Exit")

        Option = input("Enter one of the options listed above: ")

        if Option == 'search':
            title = input("Enter the book title to search: ")
            library.searchBookTitle(title)

        elif Option == 'add':
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            isbn = input("Enter the ISBN: ")
            book = Book(title, author, isbn)
            library.add_books(book)

        elif Option == 'display':
            library.displayAvailableBooks()


        elif Option == 'check out':
            isbn = input("Enter the book ISBN to check out: ")
            library.check_out(isbn)

        elif Option == 'check in':
            isbn = input("Enter the book ISBN to check in: ")
            library.check_in(isbn)

        elif Option == 'exit':
            print("You are now exiting the library management system.")
            break

        else:
            print("Invalid option. Please enter one of the given choices.")


# Runs the Library Management System
if __name__ == '__main__':
    main()
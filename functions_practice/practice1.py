
# Build a Library Management System using functions where:

# Books are stored in a list

# User can:

# Add a book

# Remove a book

# Search a book

# Display all books

# System runs until user exits





library = []

def add_book(book):
    library.append(book)
    print(f"{book} added successfully")

def remove_book(book):
    if book in library:
        library.remove(book)
        print(f"{book} removed successfully")
    else:
        print("Book not found")

def search_book(book):
    if book in library:
        print("Book available")
    else:
        print("Book not available")

def display_books():
    if not library:
        print("Library is empty")
    else:
        print("Books in Library:")
        for book in library:
            print("-", book)

while True:
    print("\n1.Add 2.Remove 3.Search 4.Display 5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_book(input("Enter book name: "))
    elif choice == "2":
        remove_book(input("Enter book name: "))
    elif choice == "3":
        search_book(input("Enter book name: "))
    elif choice == "4":
        display_books()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
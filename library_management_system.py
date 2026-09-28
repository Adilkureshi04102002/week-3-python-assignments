class Library:
    def __init__(self):
        self.books = []

    # Add a book
    def add_book(self, book):
        self.books.append({"name": book, "issued": False})
        print(book, "added successfully.")

    # Remove a book
    def remove_book(self, book):
        for b in self.books:
            if b["name"] == book:
                if b["issued"]:
                    print("Book is currently issued and cannot be removed.")
                else:
                    self.books.remove(b)
                    print(book, "removed successfully.")
                return

        print("Book not found.")

    # Issue a book
    def issue_book(self, book):
        for b in self.books:
            if b["name"] == book:
                if b["issued"]:
                    print("Book is already issued.")
                else:
                    b["issued"] = True
                    print(book, "issued successfully.")
                return

        print("Book not found.")

    # Return a book
    def return_book(self, book):
        for b in self.books:
            if b["name"] == book:
                if b["issued"]:
                    b["issued"] = False
                    print(book, "returned successfully.")
                else:
                    print("Book was not issued.")
                return

        print("Book not found.")

    # Display books
    def display_books(self):
        print("\nLibrary Books:")

        if len(self.books) == 0:
            print("No books available.")
            return

        for b in self.books:
            if b["issued"]:
                print(b["name"], "- Issued")
            else:
                print(b["name"], "- Available")


# Create Library object
library = Library()

# Add books
library.add_book("Python Programming")
library.add_book("Java Programming")
library.add_book("Data Structures")

# Display books
library.display_books()

# Issue a book
library.issue_book("Python Programming")

# Display books
library.display_books()

# Return a book
library.return_book("Python Programming")

# Display books
library.display_books()

# Remove a book
library.remove_book("Java Programming")

# Display final books
library.display_books()
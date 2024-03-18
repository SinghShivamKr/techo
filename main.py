from book import Library
from user import UserManager
from check import CheckoutManager

class LibraryManagementSystem:
    """
    Library Management System class to manage library operations.

    Attributes:
        library (Library): Instance of the Library class.
        user_manager (UserManager): Instance of the UserManager class.
        checkout_manager (CheckoutManager): Instance of the CheckoutManager class.
    """

    def __init__(self):
        """
        Initialize the LibraryManagementSystem with instances of Library, UserManager, and CheckoutManager.
        """
        self.library = Library()
        self.library.load_books()
        self.user_manager = UserManager()
        self.user_manager.load_users()
        self.checkout_manager = CheckoutManager()
        self.checkout_manager.load_checkouts()

    def main_menu(self):
        """
        Display the main menu options and prompt the user for their choice.

        Returns:
            str: The user's choice.
        """
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Add User")
        print("4. Checkout Book")
        print("5. Exit")
        choice = input("Enter choice: ")
        return choice

    def run(self):
        """
        Run the main loop of the Library Management System.
        """
        while True:
            choice = self.main_menu()
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.list_books()
            elif choice == '3':
                self.add_user()
            elif choice == '4':
                self.checkout_book()
            elif choice == '5':
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")

    def add_book(self):
        """
        Add a book to the library.
        """
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        if title and author and isbn:
            self.library.add_book(title, author, isbn)
            print("Book added.")
        else:
            print("Invalid input. Please provide title, author, and ISBN.")

    def list_books(self):
        """
        List all books in the library.
        """
        self.library.list_books()

    def add_user(self):
        """
        Add a user to the system.
        """
        name = input("Enter user name: ")
        user_id = input("Enter user ID: ")
        if name and user_id:
            self.user_manager.add_user(name, user_id)
            print("User added.")
        else:
            print("Invalid input. Please provide name and user ID.")

    def checkout_book(self):
        """
        Checkout a book from the library.
        """
        user_id = input("Enter user ID: ")
        isbn = input("Enter ISBN of the book to checkout: ")
        if user_id and isbn:
            self.checkout_manager.checkout_book(user_id, isbn)
            print("Book checked out.")
        else:
            print("Invalid input. Please provide user ID and ISBN.")

if __name__ == "__main__":
    library_system = LibraryManagementSystem()
    library_system.run()

import json

class Checkout:
    def __init__(self, user_id, isbn):
        """
        Initialize a Checkout object with user ID and ISBN.

        Args:
            user_id (str): The ID of the user checking out the book.
            isbn (str): The ISBN of the book being checked out.
        """
        self.user_id = user_id
        self.isbn = isbn

class CheckoutManager:
    def __init__(self, storage_file="checkouts.json"):
        """
        Initialize a CheckoutManager object with a storage file for checkouts.

        Args:
            storage_file (str, optional): The file path for storing checkout data. Defaults to "checkouts.json".
        """
        self.storage_file = storage_file
        self.checkouts = []

    def checkout_book(self, user_id, isbn):
        """
        Checkout a book and save the checkout information.

        Args:
            user_id (str): The ID of the user checking out the book.
            isbn (str): The ISBN of the book being checked out.
        """
        if self._validate_input(user_id, isbn):
            self.checkouts.append(Checkout(user_id, isbn))
            self._save_checkouts()
        else:
            print("Error: Invalid user ID or ISBN. Checkout failed.")

    def _save_checkouts(self):
        """Save the list of checkouts to the storage file."""
        try:
            with open(self.storage_file, 'w') as file:
                json.dump([vars(checkout) for checkout in self.checkouts], file)
        except Exception as e:
            print(f"Error saving checkouts: {e}")

    def load_checkouts(self):
        """Load the list of checkouts from the storage file."""
        try:
            with open(self.storage_file, 'r') as file:
                data = json.load(file)
                self.checkouts = [Checkout(**checkout_data) for checkout_data in data]
        except FileNotFoundError:
            self.checkouts = []
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

    def _validate_input(self, user_id, isbn):
        """
        Validate the input for user ID and ISBN.

        Args:
            user_id (str): The ID of the user.
            isbn (str): The ISBN of the book.

        Returns:
            bool: True if input is valid, False otherwise.
        """
        if not user_id or not isbn:
            print("User ID and ISBN cannot be empty.")
            return False
        # Add more validation rules as needed
        return True

# Usage example:
# checkout_manager = CheckoutManager()
# checkout_manager.load_checkouts()
# checkout_manager.checkout_book("user123", "978-3-16-148410-0")


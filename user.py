import json

class User:
    def __init__(self, name, user_id):
        """
        Initialize a User object with a name and user ID.

        Args:
            name (str): The name of the user.
            user_id (str): The ID of the user.
        """
        self.name = name
        self.user_id = user_id

class UserManager:
    def __init__(self, storage_file="users.json"):
        """
        Initialize a UserManager object with a storage file for user data.

        Args:
            storage_file (str, optional): The file path for storing user data. Defaults to "users.json".
        """
        self.storage_file = storage_file
        self.users = []

    def add_user(self, name, user_id):
        """
        Add a new user to the UserManager and save the user data.

        Args:
            name (str): The name of the user.
            user_id (str): The ID of the user.
        """
        if self._validate_input(name, user_id):
            self.users.append(User(name, user_id))
            self._save_users()

    def _save_users(self):
        """Save the list of users to the storage file."""
        try:
            with open(self.storage_file, 'w') as file:
                json.dump([vars(user) for user in self.users], file)
        except Exception as e:
            print(f"Error saving users: {e}")

    def load_users(self):
        """Load the list of users from the storage file."""
        try:
            with open(self.storage_file, 'r') as file:
                data = json.load(file)
                self.users = [User(**user_data) for user_data in data]
        except FileNotFoundError:
            self.users = []
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

    def _validate_input(self, name, user_id):
        """
        Validate the input for name and user ID.

        Args:
            name (str): The name of the user.
            user_id (str): The ID of the user.

        Returns:
            bool: True if input is valid, False otherwise.
        """
        if not name or not user_id:
            print("Name and user ID cannot be empty.")
            return False
        # Add more validation rules as needed
        return True

# Usage example:
# user_manager = UserManager()
# user_manager.load_users()
# user_manager.add_user("John Doe", "JD123")

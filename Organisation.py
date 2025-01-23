from Suppliers import Suppliers
from Users import Users
from InvalidUserError import InvalidUserError

class Organisation:
    def __init__(self, suppliers, users):
        self.suppliers = suppliers
        self.users = users

    # Add this method to provide access to the suppliers
    def get_suppliers(self):
        return self.suppliers

    def use(self):
        print("Welcome to the Prog2 Warehouse Manager")
        while True:
            try:
                # Ask the user to login
                print("Please login below:")
                username = input("Username: ")
                password = input("Password: ")

                # Validate the user
                user = self.users.validate_user(username, password)

                # Now let the user interact with the system
                user.use(self)
                break  # This breaks out of the while loop after the user logs out

            except InvalidUserError:
                print("No user found! Try again? (y/n): ", end="")
                retry = input()
                if retry.lower() != 'y':
                    break  # Exit the loop if the user doesn't want to try again

        # Ensure this final message is printed after exiting the loop
        print("Thanks for using the Prog2 Warehouse Manager. Come again soon!")

if __name__ == "__main__":
    # Seed the suppliers and users
    seeded_suppliers = Suppliers().seed_data()
    seeded_users = Users().seed_data(seeded_suppliers)
    Organisation(seeded_suppliers, seeded_users).use()



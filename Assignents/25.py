# Define a custom exception class
class MenuOptionError(Exception):
    def __init__(self, message="Invalid menu option selected"):
        self.message = message
        super().__init__(self.message)


def menu():
    print("Menu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")


def get_user_choice():
    choice = input("Enter your choice (1/2/3): ")
    return choice


try:
    menu()
    user_choice = get_user_choice()

    if user_choice == '1':
        raise MenuOptionError()

  

except MenuOptionError as e:
    print(f"Error: {e}")
else:
    print("Menu option processed successfully.")
    
             
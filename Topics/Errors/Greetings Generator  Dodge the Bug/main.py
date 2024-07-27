# Import necessary library for user input
import sys

def greet_user():
    # Get the user's name from command line input
    name = input()

    # Print a greeting message
    print(f"Hello, {name}!")

# Check if the script is the main entry point
if __name__ == '__main__':
    greet_user()

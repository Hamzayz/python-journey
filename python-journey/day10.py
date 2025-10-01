# DAY 10: FUNCTIONS WITH OUTPUTS AND CALCULATOR PROJECT
# This file covers function returns, function composition, and a calculator project

# IMPORTING MODULES:
import sys  # For program exit functionality

# FUNCTIONS WITH OUTPUTS:
# Functions can return values using the 'return' statement
# The return statement ends the function execution and sends back a value

# Example 1: Basic Function with Return
def format_name(f_name, l_name):
    format_f_name = f_name  # Store first name
    format_l_name = l_name  # Store last name
    # Return formatted full name using f-string
    return f"{format_f_name} {format_l_name}"

# Example 2: String Method Usage
def format_name_1(title):
    # title() method capitalizes first letter of each word
    return title.title()

# Function Composition:
# Using the output of one function as input to another
full_name = format_name_1(format_name("muhammAd", "HAMZA"))
print(full_name)

# PROJECT: CALCULATOR WITH CONTINUOUS OPERATIONS
# This project demonstrates function organization and dictionary usage

# Basic Arithmetic Functions:
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def division(n1, n2):
    return n1 / n2

def multiplication(n1, n2):
    return n1 * n2

# Dictionary of Operations:
# Maps operation symbols to their corresponding functions
operations = {
    "+": add,
    "-": sub,
    "/": division,
    "*": multiplication
}

# Main Calculator Function:
def calculator():
    print("Welcome to our calculator!")
    continues = True
    # Get initial number
    num_1 = int(input("Type your first number: "))

    # Main calculation loop
    while continues:
        # Display available operations
        for symbol in operations:
            print(symbol)
        
        # Get operation and second number
        operation = input("What operation you want to do: ")
        num_2 = int(input("Type your second number: "))

        # Perform calculation using the operation dictionary
        answer = operations[operation](num_1, num_2)
        print(f"{num_1} {operation} {num_2} = {answer}")

        # Ask user what to do next
        choice = input(f"Type 'y' to continue with {answer} or \n"
                      f"Type 'n' to continue with new calculation or \n"
                      f"Type 'x' to close the calculator . ")
        
        if choice == "y":
            # Continue with the answer as first number
            num_1 = answer
        elif choice == "n":
            # Start new calculation
            continues = False
            print("\n" * 30)  # Clear screen
            calculator()
        else:
            # Exit calculator
            continues = False
            print("Bye")
            sys.exit()

# Start the calculator
calculator()
# DAY 8: FUNCTIONS WITH PARAMETERS AND THE CAESAR CIPHER PROJECT
# This file covers function parameters, arguments, and a practical encryption project

# BASIC FUNCTION DEFINITION:
# A function is a block of reusable code that performs a specific task
def greet():
    print("Hello!")
    print("How are you.")
    print("I am also fine.")
greet()  # Function call without parameters

# FUNCTIONS WITH PARAMETERS:
# Parameters are variables that receive values when the function is called
def greet_with_name(name):  # 'name' is the parameter
    print(f"Hello {name}!")  # f-string for string formatting
    print(f"How are you.{name}")
    print(f"I am also fine {name}.")
greet_with_name("hamza")  # "hamza" is the argument

# PARAMETERS VS ARGUMENTS:
# - Parameters: Variables defined in the function definition
# - Arguments: Actual values passed to the function when called
# Parameters act as placeholders for values that will be passed into the function

# FUNCTIONS WITH MULTIPLE PARAMETERS:
# Functions can accept multiple parameters separated by commas
def great_name_place(name, place):
    print(f"Hello {name}")
    print(f"Are you from {place}")
great_name_place("hamza", "peshawer")

# KEYWORD ARGUMENTS:
# Using parameter names when calling functions allows arguments to be passed in any order
def great_name_places(name, place):
    print(f"Hello {name}")
    print(f"Are you from {place}")
# Keyword arguments make the code more readable and less prone to ordering errors
great_name_place(place="peshawer", name="hamza")

# PROJECT: CAESAR CIPHER
# A simple encryption/decryption program that shifts letters in the alphabet
print("Welcome to code maker!")

# Define the alphabet for the cipher
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Main program loop
should_continue = True
while should_continue:
    # Get user input for encryption/decryption
    direction = input("Type 'encord' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # CAESAR CIPHER FUNCTION:
    # Parameters:
    # - original_text: The message to encrypt/decrypt
    # - shift_amount: Number of positions to shift letters
    # - encode_or_decode: Direction of the shift
    def caesar(original_text, shift_amount, encode_or_decode):
        # For decoding, reverse the shift direction
        if encode_or_decode == "decode":
            shift_amount *= -1

        caesar_text = ""  # Initialize result string
        for latter in original_text:
            if latter not in alphabets:
                caesar_text += latter  # Keep non-alphabet characters unchanged
            # Process letters that are in the alphabet
            if latter in alphabets:
                # Calculate new position after shift
                shifted_position = alphabets.index(latter) + shift_amount
                # Use modulo to wrap around the alphabet
                shifted_position %= len(alphabets)
                caesar_text += alphabets[shifted_position]
            else:
                # Keep non-alphabet characters unchanged
                caesar_text += latter

        print(f"Here is the {encode_or_decode}d result: {caesar_text}")

    # Call the caesar function with user inputs
    caesar(text, shift, direction)
    
    # Ask if user wants to continue
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Good Bye")

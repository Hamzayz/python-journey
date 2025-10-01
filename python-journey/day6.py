# DAY 6: FUNCTIONS, CODE BLOCKS AND WHILE LOOPS
# This file covers Python functions, code blocks, and while loop implementation

# FUNCTIONS IN PYTHON:
# Functions are reusable blocks of code that perform specific tasks
# They help in organizing code and reducing repetition

# Defining a custom function
def my_function():  # Function definition using 'def' keyword
    print("hello")  # First statement in the function
    print("world")  # Second statement in the function

# Function call to execute the code inside the function
my_function()  # This will print "hello" followed by "world"

# Example 1: Function with parameters
def greet(name):
    print(f"Hello, {name}! Welcome to Python!")

# Calling function with different arguments
greet("Alice")
greet("Bob")

# Example 2: Function with return value
def calculate_square(number):
    return number * number

# Using the return value
result = calculate_square(5)
print(f"Square of 5 is: {result}")

# Example 3: Function with multiple parameters
def calculate_rectangle_area(length, width):
    return length * width

# Using multiple parameters
area = calculate_rectangle_area(4, 6)
print(f"Area of rectangle: {area}")

# WHILE LOOPS:
# While loops execute code repeatedly as long as a condition is true
# Unlike for loops, while loops continue until the condition becomes false

# Example of a while loop with a counter
friends = ["Alice", "Bob", "Charlis", "David", "Emanuel"]
n = 0  # Initialize counter
while n <= 3:  # Loop continues while n is less than or equal to 3
    print(n)  # Print current value of n
    n += 1    # Increment n by 1 in each iteration

# Example 4: While loop with user input
def number_guessing_game():
    import random
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                return

            print(f"Attempts remaining: {max_attempts - attempts}")

        except ValueError:
            print("Please enter a valid number!")
            continue

    print(f"Game Over! The number was {secret_number}")

# Example 5: While loop with break and continue
def password_checker():
    correct_password = "python123"
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        password = input("Enter password: ")
        attempts += 1

        if password == correct_password:
            print("Access granted!")
            break
        else:
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Wrong password! {remaining} attempts remaining.")
            else:
                print("Access denied! No more attempts.")

# PROJECT: Simple Calculator with Menu
def calculator():
    print("\n=== Simple Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            
            if choice == 5:
                print("Thank you for using the calculator!")
                break
                
            if choice not in [1, 2, 3, 4]:
                print("Invalid choice! Please select 1-5.")
                continue

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == 2:
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == 3:
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == 4:
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")

        except ValueError:
            print("Invalid input! Please enter numbers only.")

# Uncomment the function calls below to run the examples
# number_guessing_game()
# password_checker()
# calculator()



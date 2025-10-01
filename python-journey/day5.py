import random
# DAY 5: LOOPS, RANGE AND CODE BLOCKS
# This file covers Python loops, range function, and code block organization

# LOOPS IN PYTHON:
# Loops allow you to execute code multiple times without repetition
# The for loop iterates over a sequence (list, tuple, string, etc.)

# Basic for loop with a list
fruits = ["apple", "peach", "mango"]
for fruit in fruits:  # Iterates through each item in the list
    print(fruit)
    print(fruit + "pie")  # String concatenation with each fruit

# Working with numerical lists
students_score = [100, 98, 67, 78, 89, 34, 55, 46]
print(sum(students_score))  # Built-in sum() function adds all numbers in list

# Manual sum calculation using a loop
sum = 0
for score in students_score:
    sum += score  # Accumulates the sum
print(sum)

# Finding maximum value using built-in function
print(max(students_score))  # max() returns the highest value in the list

# Manual maximum calculation using a loop
max_score = 0
for score in students_score:
    if score > max_score:
        max_score = score  # Updates max_score if current score is higher
print(max_score)

# RANGE FUNCTION:
# range() generates a sequence of numbers
# Syntax: range(start, stop, step)
# - start: beginning number (inclusive)
# - stop: ending number (exclusive)
# - step: increment between numbers (optional)

# Basic range usage
for number in range(1, 10):  # Prints numbers 1 through 9
    print(number)

# Range with step parameter
for number in range(1, 10, 3):  # Prints numbers with step of 3: 1, 4, 7
    print(number)

# Sum of numbers from 1 to 100
total = 0
for number in range(1, 101):
    total += number
print(total)

# Repeating a string multiple times
nam = "hamza"
for name in range(3):  # Prints "hamza" three times
    print(nam)

# PASSWORD GENERATOR PROJECT:
# This project creates a random password based on user specifications

# Define character sets for password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Get user input for password composition
user_letter = int(input("How many latters do you want?\n"))
user_symbols = int(input("How many symbols do you want?\n"))
user_number = int(input("How many numbers do you want?\n"))

# Initialize empty password list
password = []

# Generate random letters
for char in range(0, user_letter):
    password += random.choice(letters)  # Adds random letter to password list

# Generate random numbers
for numb in range(0, user_number):
    password += random.choice(numbers)

# Generate random symbols
for symb in range(0, user_symbols):
    password += random.choice(symbols)

# Shuffle the password characters for randomness
random.shuffle(password)  # random.shuffle() only works with lists

# Convert list to string
passwords = ""
for chat in password:
    passwords += chat

# Display the generated password
print(f"Your passward is :{passwords}")


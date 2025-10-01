# DAY 4: RANDOMIZATION AND PYTHON LISTS
# This file covers random number generation and list manipulation in Python

# RANDOM MODULE:
# The random module provides various functions for generating random numbers
# Different types of random generation:
# - random.choice(): Picks random element from a sequence
# - random.randint(): Generates random integer in a range
# - random.random(): Generates random float between 0.0 and 1.0
import random   # Import statement must be at the top

# Random Integer Generation
random_integers = random.randint(1, 10)  # Generates random number between 1 and 10 (inclusive)
print(random_integers)

# Random Float Generation
random_float = round(random.random(), 2)  # Generates random float between 0.0 and 1.0, rounded to 2 decimals
print(random_float)
random_float1 = round(random.uniform(1, 10), 2)  # Generates random float between 1 and 10
print(random_float1)

# Simple Heads or Tails Game
random_2 = random.randint(1, 2)
if random_2 == 1:
    print("Heads!")
else:
    print("Tails!")

# LISTS IN PYTHON:
# Lists are ordered, mutable collections that can store multiple items
provinces = ["Punjab", "Sindh", "Khyber Pakhtunkhwa", "Balochistan"]  # Creating a list
provinces[-2] = "KPK"  # Modifying list element using negative indexing
provinces.append("Peshawer")  # Adding element to end of list
provinces.pop(0)  # Removing element at index 0
provinces.extend(["islamabad", "lahore"])  # Adding multiple elements to list
print(provinces)
print(provinces[-3])  # Accessing element using negative indexing

# List Operations with Random Selection
friends = ["Alice", "Bob", "Charlis", "David", "Emanuel"]
name = random.randint(0, 4)  # Method 1: Using random index
print(friends[name])
print(random.choice(friends))  # Method 2: Using random.choice()

# Nested Lists
provinces_friends = (provinces, friends)  # Creating a tuple of lists
print(provinces_friends)

# Common List Errors:
# IndexError: Occurs when trying to access an index that doesn't exist
print(len(friends))  # Getting length of list (5 elements, but indices are 0-4)

# PROJECT: Rock Paper Scissors Game
print("Welcome to rock paper sissore Game!")
game = ["Rock", "Paper", "Sissor"]
user_choice = int(input("What do you chose?type 0 for rock, 1 for paper, 2 for siccor.\n"))

# Input validation
if user_choice >= 0 and user_choice <= 2:
    print("Your choice is:")
    print(game[user_choice])

# Computer's choice
computer_choice = random.randint(0, 2)
print("Computer choice is:")
print(game[computer_choice])

# Game logic
if user_choice < 0 or user_choice >= 3:
    print("you write invalid no")
elif user_choice == 0 and computer_choice == 2:  # Rock beats Scissors
    print("You win!")
elif computer_choice == 0 and user_choice == 2:  # Scissors loses to Rock
    print("You lose!")
elif user_choice > computer_choice:  # Higher index wins (Paper > Rock, Scissors > Paper)
    print("You win!")
elif computer_choice > user_choice:  # Higher index wins
    print("You lose!")
elif user_choice == computer_choice:  # Same choice means draw
    print("It's Draw!")




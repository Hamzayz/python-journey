# DAY 12: NAMESPACES, SCOPE, AND NUMBER GUESSING GAME
# This file covers variable scope, namespaces, and a number guessing game project

# NAMESPACES AND SCOPE:
# Scope determines where variables can be accessed in your code
# Python has two main types of scope: Local and Global

# LOCAL SCOPE:
# Variables defined inside a function are in local scope
# They can only be accessed within that function
enemie = 1  # Global variable

def name():
    enemie = 2  # Local variable (different from global enemie)
    print(f"enemie inside function: {enemie}")  # Output: 2 (uses local variable)

name()
print(f"enemie outside function: {enemie}")  # Output: 1 (uses global variable)

# GLOBAL SCOPE:
# Variables defined outside functions are in global scope
# They can be accessed from anywhere in the code
health_player = 10  # Global variable

def drink_potion():
    portion_stringth = 2  # Local variable
    print(health_player)  # Can access global variable

drink_potion()

# MODIFYING GLOBAL SCOPE:
# To modify a global variable inside a function, you need to:
# 1. Use the 'global' keyword, or
# 2. Return the new value and reassign it
health_player = 10  # Global variable

def drink_potion(score):
    print(health_player)
    return health_player + 1  # Return new value instead of modifying global directly

print(drink_potion(health_player))

# GLOBAL CONSTANTS:
# Variables that should not be changed are typically written in UPPERCASE
# This is a naming convention to indicate they are constants
PI = 3.14159  # Constant value

# PROJECT: NUMBER GUESSING GAME
print("\n" * 30)  # Clear screen
import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
random_num = random.randint(0, 100)  # Generate random number

# Game Setup:
# Get difficulty level and set attempts accordingly
lavel = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
if lavel == "easy":
    attempts += 10  # Easy mode: 10 attempts
elif lavel == "hard":
    attempts += 5   # Hard mode: 5 attempts

# Main Game Loop:
continues = True
while continues:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    # Check if guess is correct
    if random_num != guess:
        attempts -= 1  # Reduce remaining attempts
        
        # Check if out of attempts
        if attempts == 0:
            continues = False
            print("No more attempts. You lose.")
            play_game = input("Do you want to play again? Type 'y' for yes and 'n' for no: ")
            if play_game == "n":
                continues = False
                print("Bye")
        # Give hints based on guess
        elif guess > random_num:
            print("Too high.")
        elif guess < random_num:
            print("Too low.")
    # Correct guess
    elif guess == random_num:
        print("It's right! You win!")
        play_game = input("Do you want to play again? Type 'y' for yes and 'n' for no: ")
        if play_game == "n":
            continues = False
            print("Bye")
# DAY 7: HANGMAN GAME PROJECT
# This project combines multiple Python concepts to create a word guessing game

# IMPORTING MODULES:
# The random module is used for selecting random words from our list
import random

# DATA STRUCTURES:
# List of words for the game
random_words = ["apple", "banana", "cat", "dog", "elephant", "fish", "grape", "hat"]

# Dictionary to store word definitions as hints
# Key: word, Value: hint/definition
dictionary = {
    "apple": "is fruit",
    "banana": "is fruit",
    "cat": "is animal",
    "dog": "is animal",
    "elephant": "is animal",
    "fish": "is animal",
    "grape": "is fruit",
    "hat": "humans ware it"
}

# GAME SETUP:
print("welcome to word gusse game!")
lives = 6  # Number of incorrect guesses allowed

# GAME INITIALIZATION:
# Select a random word from the list
random_word = random.choice(random_words)
length = len(random_word)  # Get the length of the chosen word

# Create placeholders for the word
# This creates a string of underscores equal to the word length
place_holder = ""
for places in range(length):
    place_holder += "_"
print(place_holder)

# GAME HINTS:
# Display word length and definition as hints
print(f"The word has {length} latter.")
print(dictionary[random_word])

# GAME LOGIC:
correct_latters = []  # List to store correctly guessed letters
game_over = False    # Flag to control game loop

# MAIN GAME LOOP:
while not game_over:
    display = ""  # String to build the current word display
    guess = input("Gusee the latter: ").lower()  # Get user input and convert to lowercase

    # Check each letter in the word
    for latter in random_word:
        if guess == latter:  # If guess matches current letter
            display += latter
            correct_latters.append(guess)
        elif latter in correct_latters:  # If letter was previously guessed
            display += latter
        else:  # If letter hasn't been guessed
            display += "_"
    print(display)

    # GAME STATE UPDATES:
    # Check if guess was incorrect
    if guess not in random_word:
        lives -= 1  # Reduce remaining lives
        if lives == 0:  # Check if game is lost
            game_over = True
            print("You lose!")

    # Check if game is won (no more underscores in display)
    if "_" not in display:
        game_over = True
        print("You win!")
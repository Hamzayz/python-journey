# DAY 13: DEBUGGING TECHNIQUES IN PYTHON
# This file demonstrates various debugging techniques and common errors

# DEBUGGING TECHNIQUE 1: DESCRIBE THE PROBLEM
# Understanding what the code is supposed to do helps identify issues
def my_function():
    # Original error: range(1, 20) would count from 1 to 19
    # Fixed: range(1, 21) to include 20
    for i in range(1, 21):
        if i == 20:
            print("Got it!")
my_function()

# DEBUGGING TECHNIQUE 2: REPRODUCE THE BUG
# Isolating the problem helps in understanding and fixing it
import random
from random import randint

# List of dice face emojis
dice_image = ["①", "②", "③", "④", "⑤", "⑥"]
# Original error: randint(1, 6) would give index out of range
# Fixed: randint(0, 5) to match list indices
dice_num = randint(0, 5)
print(dice_image[dice_num])

# DEBUGGING TECHNIQUE 3: HANDLING USER INPUT ERRORS
# Using try-except to handle invalid input gracefully
try:
    age = int(input("How old are you? "))
except ValueError:
    # Handle non-numeric input
    print("You write an invalid number try again.")
    age = int(input("How old are you? "))

# Original error: Missing 'f' in f-string
# Fixed: Added 'f' to properly format the string
if age > 18:
    print(f"You can drive at age {age}.")
elif age < 18:
    print(f"You can't drive at age {age}.")

# DEBUGGING TECHNIQUE 4: USING PRINT STATEMENTS
# Adding print statements to track variable values
word_per_page = 0
pages = int(input("Number of pages: "))
# Original error: Using == (comparison) instead of = (assignment)
# Fixed: Changed == to = for assignment
word_per_page = int(input("number of words per page: "))
total_words = word_per_page * pages

# Debug prints to check variable values
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")
print(f"total_words = {total_words}")

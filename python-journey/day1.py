# DAY 1: PYTHON BASICS
# This file covers fundamental Python concepts including printing, variables, and user input

# Basic Print Statement
print("HELLO WORLD!")  # Basic way to display text on screen

# String Manipulation
print("HELLO WORLD!\nhello world")  # \n creates a new line
print("HELLO"+"WORLD")  # String concatenation (joining strings)
print("HELLO"+" "+"WORLD")  # Adding space between concatenated strings

# User Input
# input() function: Pauses program and waits for user to type something
# The text inside input() is the prompt shown to the user
print("Hello"+" "+input("what is your name?")+"!")  # Using input in print statement

# Variables
# Variables are containers for storing data values
name = "hamza"  # Creating a variable and assigning a value
print(name)  # Displaying variable content

# Dynamic Variable Assignment
name = input("what is your name?")  # Storing user input in a variable
print(name)

# String Length
length = len(name)  # len() function returns the length of a string
print(length)
print(len(input("what is your name?")))  # Getting length directly from input

# Variable Naming Rules:
# 1. No spaces allowed (use underscore: user_name)
# 2. Can't start with numbers (name1 is valid, 1name is not)
# 3. Case sensitive (name and Name are different variables)

# PROJECT 1: Band Name Generator
name = input("what is your name?\n")  # \n creates new line in input prompt
print("Hello "+ name)
print("Welcome to the band name generator.")
city = input("What is the name of your city?\n")
pet_name = input("what is the name of your pet?\n")
print("Your band name is "+ city+" "+pet_name)

# PROJECT 2: User Information Collector
print("Welcome to the best talk!")
print("Give us some information about yourself.\n")
name = input("What is your name?\n")
length = str(len(name+"\n"))  # Converting length to string for concatenation
age = str(input("What is your age?\n"))  # Converting age to string
colour = input("What is your favorite colour?\n")
# Using string concatenation to create a detailed output
print("So, Your name is "+ name +" and your name consist of "+(length)+" latters.\nYour are "+age+" years old."+"Your favorite colour is "+colour+".")

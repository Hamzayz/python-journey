# DAY 2: DATA TYPES AND MATHEMATICAL OPERATIONS
# This file covers Python data types, type conversion, and mathematical operations

# DATA TYPES:
# 1. STRINGS: Sequence of characters, enclosed in quotes ("hamza")
# 2. INTEGER: Whole numbers without decimal points (123)
# 3. FLOAT: Numbers with decimal points (3.3)
# 4. BOOLEAN: True or False values, used for conditions

# String Indexing
print("hello"[0])  # Gets first character (index 0)
print("hello"[-1])  # Gets last character (negative indexing)

# Number Operations
print(123+456)  # Addition of integers
print(len(str(12345)))  # Converting number to string to get length

# Type Checking
print(type("hamza"))  # Shows <class 'str'>
print(type(12345))    # Shows <class 'int'>
print(type(2.5))      # Shows <class 'float'>
print(type(True))     # Shows <class 'bool'>

# Type Conversion Functions
str()   # Converts to string
int()   # Converts to integer
float() # Converts to float
bool()  # Converts to boolean

# String Length with Input
print("number of latter in your name:"+ str(len(input("enter your name"))))

# MATHEMATICAL OPERATIONS:
print(123+456)  # Addition
print(456-123)  # Subtraction
print(12*34)    # Multiplication
print(4/2)      # Division (returns float)
print(type(4//2))  # Integer division (removes decimal)
print(2**3)     # Exponentiation (2 to power 3)

# PEMDAS (Order of Operations):
# Parentheses (), Exponents **, Multiplication */Division /, Addition +/Subtraction -
print(3*(3+3)/3-3)

# BMI Calculation Example
bmi = 84/1.65**2
print(int(bmi))        # Removes decimal places
print(round(bmi))      # Rounds to nearest integer
print(round(bmi, 2))   # Rounds to 2 decimal places

# Number Manipulation Operators:
# += (add and assign)
# -= (subtract and assign)
# *= (multiply and assign)
# /= (divide and assign)
score = 0
score += 1  # Same as: score = score + 1
print(score)

# F-STRINGS (Formatted String Literals):
# Allows embedding expressions inside string literals
score = 10
hight = 6
is_winning = True
print(f"Your score is {score}. Your hight is {hight}. Your winning is {is_winning}.")

# PROJECT 1: Tip Calculator
print("Welcome to the tip calculator!")
total_bill = int(input("What are the total bill?"))
tip = int(input("How much tip would you want to give?"))
people = int(input("How much people to split the bill?"))

bill_tip = (tip/100)*total_bill + total_bill
people_slit = bill_tip/people
print(round(people_slit, 2))

# PROJECT 2: Profit Splitter
print("Welcome to the Profit Splitor!")
print("Before splitting the profit i want some information!")
name = input("What is your name?\n")
age = input("what is your age?\n")
live = input("where do you live?\n")
print(f"your name is {name}. Your age is {age} and you live in {live}.")

print("Now we will continue to split your profit.")
people = input("How much people to split in?\n")
profit = int(input("How much profit to split?\n"))
persent_1 = int(input("How much first person he will have?\n"))
persent_2 = int(input("How much second person he will have?\n"))
persent_3 = int(input("How much third person he will have?\n"))

# Calculating each person's share
person_1 = (persent_1//100)*profit
person_2 = (persent_2//100)*profit
person_3 = (persent_3//100)*profit

print(f"First person will have {person_1}.\nSecond person will have{person_2}.\nThird person will have {person_3}.")


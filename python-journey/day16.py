# DAY 16: OBJECT-ORIENTED PROGRAMMING (OOP) AND EXTERNAL PACKAGES
# This file demonstrates OOP concepts and using external packages in Python

# OBJECT-ORIENTED PROGRAMMING (OOP):
# OOP is a programming paradigm that organizes code into reusable, self-contained objects
# Key OOP Concepts:
# 1. Classes: Blueprints for creating objects
# 2. Objects: Instances of classes that contain data and methods
# 3. Attributes: Variables that store data about the object
# 4. Methods: Functions that define what the object can do

# Example 1: Creating a Simple Class
class Dog:
    # Class attributes (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor method (__init__) - called when creating a new instance
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Creating instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Using the instances
print("\nExample 1: Dog Class")
print(f"Dog 1: {dog1.description()}")
print(f"Dog 2: {dog2.speak('Woof!')}")
print(f"Both dogs are {Dog.species}")  # Accessing class attribute

# Example 2: Inheritance
class Bulldog(Dog):  # Bulldog inherits from Dog
    def speak(self, sound="Woof!"):  # Override the speak method
        return f"{self.name} says {sound} in a deep voice"

# Creating an instance of Bulldog
bulldog = Bulldog("Rocky", 4)
print("\nExample 2: Inheritance")
print(f"Bulldog: {bulldog.speak()}")

# Example 3: Encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        # Private attributes (convention: start with underscore)
        self._account_number = account_number
        self._balance = balance
    
    # Getter method
    def get_balance(self):
        return self._balance
    
    # Setter method with validation
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

# Creating and using a bank account
account = BankAccount("12345", 1000)
print("\nExample 3: Encapsulation")
print(f"Initial balance: ${account.get_balance()}")
account.deposit(500)
print(f"After deposit: ${account.get_balance()}")

# Example 4: PrettyTable Package
# PrettyTable is an external package for creating formatted tables
# First, install it using: pip install prettytable

from prettytable import PrettyTable

# Creating a new table object
table = PrettyTable()

# Adding columns to the table
# Each column has a header and a list of values
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Setting table alignment
# 'l' for left alignment
table.align = "l"

# Displaying the table
print("\nExample 4: PrettyTable")
print(table)

# OOP CONCEPTS DEMONSTRATED:
# 1. Encapsulation: Data and methods are bundled together
#    - PrettyTable object contains both data (columns) and methods (add_column)
#    - BankAccount class hides internal data and provides controlled access
# 2. Inheritance: Classes can inherit attributes and methods from parent classes
#    - Bulldog inherits from Dog and overrides the speak method
# 3. Abstraction: Complex operations are hidden behind simple interfaces
#    - We don't need to know how PrettyTable formats the data internally
#    - BankAccount hides the complexity of balance management
# 4. Polymorphism: Different classes can implement the same method differently
#    - Both Dog and Bulldog have a speak method, but they behave differently

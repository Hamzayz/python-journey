# Class inheritance, slicing

# Class inheritance allows a class to inherit attributes and methods from another class (parent class).
# The child class can use, modify, or extend the parent's functionality while adding its own features.

class Animal:
    def __init__(self):
        self.num_eye = 2

    def breathe(self):
        print("Inhale, Exhale.")

class Fish(Animal): # import the class "Animal"
    def __init__(self):
        super().__init__() # super means Animal class
        
    def breathe(self):
        super().breathe() # appending some informatiom to the method from different class
        print("doing this underwater.")

    def swim(self):
        print("moving in water")

nemo = Fish()
nemo.breathe()

# Slicing in Python
# Slicing is a way to extract a portion of a sequence by specifying a range of indices.
# It works with strings, lists, tuples, and other sequence types.

# 1. List Slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)

# Get a portion of the list
portion = numbers[2:5]  # Get elements from index 2 to 4
print(portion)  # Output: [2, 3, 4]


# Reverse the string
reversed_message = numbers[::-1]
print( reversed_message)  # Output: "9876543210"
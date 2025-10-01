# DAY 9: DICTIONARIES AND NESTING IN PYTHON
# This file covers dictionary operations, nesting, and a practical bidding project

# DICTIONARY BASICS:
# Dictionaries store key-value pairs where each key maps to a value
# Keys must be unique and immutable (strings, numbers, or tuples)
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

# Accessing Dictionary Values:
# Use square brackets with the key to access values
# Note: Using a non-existent key raises a KeyError
print(dictionary["banana"])

# Adding New Key-Value Pairs:
# Simply assign a value to a new key
dictionary["cloths"] = "human ware it "
print(dictionary["cloths"])

# Creating Empty Dictionary:
empty_dictionary = {}

# Modifying Dictionary:
# Wipe entire dictionary
# dictionary = {}
# print(dictionary)

# Edit existing key-value pair
dictionary["apple"] = "human eat it for energy"
print(dictionary["apple"])

# ITERATING THROUGH DICTIONARIES:
# Loop through keys and access values
for key in dictionary:
    print(key)  # Print only keys
    print(dictionary[key])  # Print values for each key

# NESTING IN PYTHON:
# Nesting allows you to store complex data structures inside other data structures
# This includes lists in dictionaries, dictionaries in lists, etc.

# Example 1: Dictionary of Capitals
capitals = {
    "pakistan": "Islamabad",
    "india": "Delhi",
    "Afghanistan": "Kabul"
}

# Example 2: Dictionary with Lists
pakistan = ["peshawer", "islamabad", "swabi"]
travel = {
    "pakistan": pakistan,  # List as a value
    "india": ["delhi", "mumbai", "bangeloro"],  # Inline list
    "afghanistan": ["kabul", "kandahar", ["ghazni", "jalalabad"]]  # Nested list
}
print(travel)

# Accessing Nested Data:
# Use multiple indices to access nested elements
print(travel["india"][2])  # Access "bangeloro"
print(travel["afghanistan"][2][0])  # Access "ghazni"

# Example 3: Dictionary within Dictionary
travel2 = {
    "pakistan": {
        "islamabad": "traveled 100 times",
        "pakistan": pakistan
    },
    "india": {
        "delhi": "traveled not many times",
        "india2": ["delhi", "mumbai", "bangeloro"],
    }
}
# Access deeply nested value
print(travel2["india"]["india2"][2])  # Access "bangeloro"

# PROJECT: SECRET AUCTION PROGRAM
print("Welcome to hidden bid!")

# Function to find the highest bidder
def find_highest_bider(bidding_dictionary):
    winner = ""
    highest_bid = 0
    # Iterate through all bidders
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        # Update winner if current bid is higher
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a highest bid of {highest_bid}")

# Main program loop
name_bid = {}  # Dictionary to store bids
continuee = True
while continuee:
    # Get bidder information
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    name_bid[name] = bid  # Store bid in dictionary
    
    # Check if more bidders
    other_people = input("Other user want to bid. type 'y' for yes and n for 'no'. ").lower()
    if other_people == "n":
        continuee = False
        find_highest_bider(name_bid)
    elif other_people == "y":
        print("\n" * 30)  # Clear screen for next bidder

# Alternative way to find highest bidder:
# print(max(name_bid, key=name_bid.get))
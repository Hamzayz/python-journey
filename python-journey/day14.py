# DAY 14: DICTIONARY OPERATIONS AND DATA STRUCTURES
# This file demonstrates dictionary usage and key-value pair manipulation

# DICTIONARY OF MOST FOLLOWED INSTAGRAM ACCOUNTS:
# A dictionary storing celebrity/brand names and their follower counts
# Using underscore (_) in numbers for better readability
most_followed_instagram = {
    "Cristiano Ronaldo": 630_000_000,  # 630 million followers
    "Lionel Messi": 504_000_000,       # 504 million followers
    "Selena Gomez": 429_000_000,       # 429 million followers
    "Kylie Jenner": 399_000_000,       # 399 million followers
    "Dwayne Johnson": 397_000_000,     # 397 million followers
    "Ariana Grande": 380_000_000,      # 380 million followers
    "Kim Kardashian": 364_000_000,     # 364 million followers
    "Beyoncé": 319_000_000,            # 319 million followers
    "Khloé Kardashian": 311_000_000,   # 311 million followers
    "Nike": 308_000_000                # 308 million followers
}

# DICTIONARY OPERATIONS:

# 1. Accessing Dictionary Elements
print("\n1. ACCESSING DICTIONARY ELEMENTS:")
# Method 1: Using square brackets
print(f"Cristiano's followers: {most_followed_instagram['Cristiano Ronaldo']}")

# Method 2: Using get() method (safer, returns None if key doesn't exist)
print(f"Messi's followers: {most_followed_instagram.get('Lionel Messi')}")

# 2. Dictionary Keys and Values
print("\n2. DICTIONARY KEYS AND VALUES:")
# Get all keys
key_list = list(most_followed_instagram.keys())
print(f"First key: {key_list[0]}")

# Get all values
value_list = list(most_followed_instagram.values())
print(f"Highest follower count: {max(value_list)}")

# 3. Dictionary Items
print("\n3. DICTIONARY ITEMS:")
# Get all key-value pairs
items_list = list(most_followed_instagram.items())
print(f"First item: {items_list[0]}")

# 4. Dictionary Modification
print("\n4. DICTIONARY MODIFICATION:")
# Adding a new key-value pair
most_followed_instagram["Taylor Swift"] = 270_000_000
print(f"Added Taylor Swift: {most_followed_instagram['Taylor Swift']}")

# Updating an existing value
most_followed_instagram["Cristiano Ronaldo"] = 631_000_000
print(f"Updated Cristiano's followers: {most_followed_instagram['Cristiano Ronaldo']}")

# 5. Dictionary Methods
print("\n5. DICTIONARY METHODS:")
# Check if key exists
print(f"Is Messi in the list? {'Lionel Messi' in most_followed_instagram}")

# Remove a key-value pair
removed_followers = most_followed_instagram.pop("Nike")
print(f"Removed Nike with {removed_followers} followers")

# 6. Dictionary Comprehension
print("\n6. DICTIONARY COMPREHENSION:")
# Create a new dictionary with only accounts having more than 400M followers
top_accounts = {name: followers for name, followers in most_followed_instagram.items() 
                if followers > 400_000_000}
print("Accounts with more than 400M followers:")
for name, followers in top_accounts.items():
    print(f"{name}: {followers:,}")

# 7. Nested Dictionaries
print("\n7. NESTED DICTIONARIES:")
# Create a nested dictionary with additional information
instagram_stats = {
    "Cristiano Ronaldo": {
        "followers": 630_000_000,
        "posts": 3400,
        "engagement_rate": "2.5%"
    },
    "Lionel Messi": {
        "followers": 504_000_000,
        "posts": 1200,
        "engagement_rate": "3.1%"
    }
}

# Accessing nested dictionary values
print(f"Messi's engagement rate: {instagram_stats['Lionel Messi']['engagement_rate']}")

# 8. Dictionary Sorting
print("\n8. DICTIONARY SORTING:")
# Sort by follower count (descending)
sorted_accounts = dict(sorted(most_followed_instagram.items(), 
                             key=lambda x: x[1], 
                             reverse=True))
print("Top 3 accounts by followers:")
for i, (name, followers) in enumerate(sorted_accounts.items(), 1):
    if i <= 3:
        print(f"{i}. {name}: {followers:,}")

# PRACTICE:
# Section 15: Day 15 - Intermediate - Local Development Environment Setup & the Coffee Machine
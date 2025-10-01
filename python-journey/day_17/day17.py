# making class
class User:
    # constructor:
    # a part of a blueprint that allows us to specify what should happen when our object is being constructed
    # initialize:
    # to set(variables) to their starting values at the beginning of a program.
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # because it is a default value 
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# Create user objects
user_1 = User("001", "hamza")
user_2 = User("002", "ilyas")

# Make user_1 follow user_2
user_1.follow(user_2)

# Print the results
print(f"User 1 followers: {user_1.followers}")
print(f"User 1 following: {user_1.following}")
print(f"User 2 followers: {user_2.followers}")
print(f"User 2 following: {user_2.following}")

# PascalCase: is a case in which we write first of words letter in capital letter "P & C"
# camelCase: is a case in which we write first letter in small and second letter in capital "c & C"
# snakecase: is a case in which we write first of words letter in small letter "s & c"

# making atttribute:
user_1.uid="13803"
print(user_1.uid)

# project:

# DAY 3: CONDITIONAL STATEMENTS AND LOGICAL OPERATORS
# This file demonstrates the use of if-else statements, logical operators, and modulo operations

# PROJECT 1: Roller Coaster Ride
# This program checks if a person can ride based on height and calculates ticket price based on age
hight=int(input("What is your hight?\n"))
if hight >= 120:
    print("You can enjoy the ride!")
    age=int(input("What is your age?\n"))
    bill=0
    # Nested if-elif-else statements to determine ticket price based on age
    if age <=12:
        bill=5
        print("child ticket 5$")
    elif age <=18:
        bill=7
        print("adult ticket 7$")
    elif age >=45 and age <=55:  # Special case for middle-aged people
        bill=0
        print("you will have free ride.")
    else:
        bill=12
        print("other ticket 12$") 
    # Optional photo add-on
    photo= input("Do you want a photo? Type Y for yes and N for no.\n")
    if photo=="Y":
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("You have to grow for a ride!")

# COMPARISON OPERATORS:
#  >     Greater than
#  <     Less than
#  >=    Greater than or Equal to
#  <=    Less than or Equal to
#  ==    Equal to
#  !=    Not equal to 

# LOGICAL OPERATORS:
#  "and"  Both conditions must be true
#  "or"   At least one condition must be true
#  "not"  The condition must be false

# MODULO OPERATION:
# "%" operator returns the remainder of a division
number=int(input("Put the number!\n"))
reminder= number % 2
if reminder == 0:  # Alternative: if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# PROJECT 2: Treasure Island Game
# A text-based adventure game with multiple choices and outcomes
print("Welcome to the treasure island!")
print("Your mission is to find the treaure!")
go=input("You are at a cross road. Where do you want to go?left or right\n")
if go=="left":
    print("You've come to the lack.There is an island in the middle of the lack.")
    wait_swim=input("Type wait to 'wait' for a boat or type 'swim' to swim across.\n")
    if wait_swim == "wait":
        print("You have arrived to the island.")
        colour=input("Choose a colour.Red blue green.\n")
        if colour=="red":
            print("There is fire!You loss.")
        elif colour=="blue":
            print("You win!")
        else:
            ("You loss!")
    if wait_swim=="swim":
        print("You have reached the three doors.")
        door=(input("choose the one door.\nfirst in which you will be shooten by army.\nsecond in which you will have 10years hungry loin.\nthird in which you will found fire.\n "))
        if door=="first":
            print("You loss!")
        elif door=="second":
            print("you win!")
        else:
            print("Game over!")
    else:
        print("Game over!")   

else:
    print("You are lost!Try again.")

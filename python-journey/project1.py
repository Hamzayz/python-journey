import random
live=5
print("Welcome to number Guess game!")
random_numb=str(random.randint(0,100))
length=len(random_numb)
print(random_numb)
#making blanks:
position=""
for number in range(length):
    position += "_"
print(position)

correct_num=[]
game_over=False
while not game_over:
    display=""
    guess=input("Guess a number: ")
    for number in random_numb:
        if number == guess:
            number += display
            correct_num.append(guess)
        elif number in correct_num:
            display += number
        else:
            display += "_"
    print(display) 

    if guess not in random_numb:
        live -= 1
        if live ==0:
            game_over=True
            print("You lose!") 

    if "_" not in display:
        game_over=True
        print("You win!")

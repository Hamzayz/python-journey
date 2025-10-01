import turtle 
import pandas

screen = turtle.Screen()
turtle.title("U.S States Game")

image = "day 25/blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("day 25/50_states.csv")
states = [state.lower() for state in data.state.to_list()]

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

guessed_states = []
game_on = True
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.lower()

    if answer_state == "exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("day 25/states_to_learn.csv")
        break

    if answer_state in states:
        guessed_states.append(answer_state)
        row = data[data.state.str.lower() == answer_state]
        x = int(row.x.item())
        y = int(row.y.item())
        writer.goto(x , y)
        writer.write(answer_state.title(), align="center", font=("Courier", 11, "italic"))

        if guessed_states == 50:
            print("Congratulations, you finished the Game")
    elif answer_state not in states:
        print("There is no such a state")


turtle.mainloop()




from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
try:
    data = pandas.read_csv("day31/data/words_to_learned.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("day31/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    data.to_dict(orient="records")
    to_learn = data.to_dict(orient="records")
current_card = {}
def next_card():
    global current_card , timer
    window.after_cancel(timer) # when ever you are clicking the buttons the timer will restart
    current_card = random.choice(to_learn)
    canves.itemconfig(card_title , text = "French" , fill="black")
    canves.itemconfig(card_word , text = current_card["French"] , fill="black" )
    canves.itemconfig(card_background, image=card_front_image)
    timer = window.after(3000 , func=flip)

def flip():
    canves.itemconfig(card_title , text = "English" , fill="white")
    canves.itemconfig(card_word , text =current_card["English"] , fill="white" )
    canves.itemconfig(card_background , image = card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn) # the data is added to words_to_learn.csv by
                                        # to_learn dictionary after the current_card is removed from it
    data.to_csv("day31/data/words_to_learned.csv" , index=False)
    next_card()


window = Tk()
window.title("Language")
window.config(padx=50 , pady=50 , bg=BACKGROUND_COLOR)

timer = window.after(3000 , func=flip)

canves = Canvas(width=800 , height=526)
card_front_image = PhotoImage(file="day31/images/card_front.png")
card_back_img = PhotoImage(file="day31/images/card_back.png")
card_background = canves.create_image(400, 263, image=card_front_image)
canves.config(bg=BACKGROUND_COLOR , highlightthickness=0)
card_title = canves.create_text(400 , 150 ,text="Title" , font=("Arial",40,"italic"))
card_word = canves.create_text(400 , 263 , text="World" , font=("Arial" , 60 , "bold"))
canves.grid(row=0 , column=0 , columnspan=2)

cross_image = PhotoImage(file="day31/images/wrong.png")
unknown_button = Button(image=cross_image , highlightthickness=0 , command=next_card)
unknown_button.grid(row=1 , column=0)

right_image = PhotoImage(file="day31/images/right.png")
right_button = Button(image=right_image , highlightthickness=0 , command=is_known)
right_button.grid(row=1 , column=1)

next_card()
window.mainloop()
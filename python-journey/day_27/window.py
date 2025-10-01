import tkinter
window = tkinter.Tk()

window.title("My first GUI Program!")
window.minsize(width=500 , height=300)
window.config(padx=20 , pady=20) # it will the labels and the buttom stay away from edges

def button_clicked():
    label.config(text = input.get())

# label :
label = tkinter.Label(text="My first label" , font=("Arial",24,"bold"))
label.grid(row=0 , column=0)
label.config(padx=30 , pady=30)

# we are changing the value of text by key word argu because it is **kwargu :
label["text"] = "My Text"

# Button
button = tkinter.Button(text="My Button" , command=button_clicked)
button.grid(row=1 , column=1)

new_button = tkinter.Button(text="My new button")
new_button.grid(row = 0 , column = 2)

# input

input = tkinter.Entry(width=10)
input.grid(row=3 , column=4)

# layout
# pack() :
    # it packs the all data and put it on window one after each we can not specify the position
    # pack(align=left or right)
# place():
    # we can enter x and y cordinates to place the data there
    # place(x = 0 , y = 0)
# grid():
    # it divide the code in to row and coloums and you can specify how many coloms and then place the text there
    # grid(row = 0 , coloum = 0)
window.mainloop()
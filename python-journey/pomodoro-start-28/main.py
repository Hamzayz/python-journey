from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
rips = 0
timr = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timr)
    canvas.itemconfig(time_text , text="00:00")
    label.config(text="Timer")
    check_mark.config(text="")
    global rips
    rips = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rips
    rips += 1

    if rips in [1,3,5,7] :
        count_down(WORK_MIN)
        label.config(text="Work" , fg=GREEN)
    if rips in [2,4,6] :
        count_down(SHORT_BREAK_MIN)
        label.config(text="Break" , fg=PINK)
    if rips in [8] :
        count_down(LONG_BREAK_MIN)
        label.config(text="Break" , fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timr
    min_count = math.floor(count / 60)
    sec_count = count % 60
    
    if sec_count < 10:
        sec_count = f"0{sec_count}"

    canvas.itemconfig(time_text ,text=f"{min_count}:{sec_count}")
    if count > 0:
        timr = window.after(1000 , count_down , count - 1)

    else:
        mark = ""
        for _ in range(math.floor(rips/2)):
            mark += "✓"
        check_mark.config(text=mark)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Time Manager")
window.config(padx=100 , pady=50 , bg=YELLOW)

label = Label(text="Timer" , font=(FONT_NAME , 40) , fg=GREEN , bg=YELLOW) 
label.grid(row=0 , column=1)
check_mark = Label( font=(FONT_NAME , 20) , fg=GREEN , bg=YELLOW)
check_mark.grid(row=4 , column=1)


Button(text="start" ,width=5 , height=1 , command=start_timer).grid(row=3 , column=0 )

Button(text="Reset" , width=5 , height=1 , command=reset).grid(row=3 , column=2)

canvas = Canvas(width=200 , height=224 , bg=YELLOW , highlightthickness=0) 
tomato_img = PhotoImage(file="pomodoro-start/tomato.png")
canvas.create_image(100 , 112 , image=tomato_img)
time_text = canvas.create_text(100 , 130 , text="00:00" ,fill="white" , font=(FONT_NAME , 35 , "bold" ) )
canvas.grid(row=1 , column=1)

window.mainloop()
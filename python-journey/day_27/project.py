import tkinter

converter = tkinter.Tk()
converter.title("Meters to KiloMeters converter")
# converter.minsize(width= 300 , height= 180)
converter.config(padx=20 , pady=20)

label = tkinter.Label(text="is equal to: ")
label.grid(row=2 , column=0)

label2 = tkinter.Label(text="0")
label2.grid(row=2 , column=1)

tkinter.Label(text="miles").grid(row=1 , column=2)
tkinter.Label(text="km").grid(row=2 , column=2)
def meter_kilo():
    value = int(input.get()) * 1.61
    label2.config(text=value)

button = tkinter.Button(text="Enter" , command=meter_kilo)
button.grid(row= 3 , column=1)

input = tkinter.Entry(width=5 )
input.grid(row=1 , column=1)

converter.mainloop()
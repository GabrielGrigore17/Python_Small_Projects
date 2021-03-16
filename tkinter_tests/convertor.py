from tkinter import *


def button_clicked():
    km = float(input_box.get())
    miles = round(km * 1.6)
    label_4.config(text=str(miles))


window = Tk()
window.title("Distance Convertor")
# window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

label_1 = Label(text="is equal to")
label_1.grid(column=0, row=1)

label_2 = Label(text="Miles")
label_2.grid(column=2, row=0)

label_3 = Label(text="Km")
label_3.grid(column=2, row=1)

label_4 = Label(text="0")
label_4.grid(column=1, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

input_box = Entry(width=10)
input_box.grid(column=1, row=0)

window.mainloop()

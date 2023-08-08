from tkinter import *

window = Tk()
window.title("Mile to Km Converter")


def calculate():
    miles = float(text_entry.get())
    km = miles * 1.609
    label2.config(text=f"{km}")

text_entry = Entry(width = 7)
text_entry.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)
label = Label()
label.configure(text="is equal to ")
label.grid(column=0,row=1)

label2 = Label()
label2.grid(column=1,row=1)
label2.configure(text="0")

label3 = Label()
label3.configure(text="Kilometers")
label3.grid(column=2,row=1)


button = Button(text="Calculate", command=calculate)
button.grid(column=1,row=2)



window.mainloop()
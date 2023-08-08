import tkinter as tk

window = tk.Tk()
window.title("My First Window")
window.minsize(width=300, height=300)
#Text is the text that will be displayed on the screen, Font is the font that will be used
label = tk.Label(text="Hello World",font = ("Arial", 20, "bold"))
# Side is the side that the text will be displayed
label.pack(side="left", expand=True)

#changes label text to text entry whenever the button is clicked
def button_clicked():
    print("Button Clicked")
    new_text = input.get()
    label.configure(text=new_text)
    label.pack(side="left", expand=True)

#create a button
button = tk.Button(text="click me", command=button_clicked)
button.pack()

#Creates a text entry field inside the window
input = tk.Entry()
input.pack()



#This keeps the window open until the user closes it
window.mainloop()



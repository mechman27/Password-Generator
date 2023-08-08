from tkinter import *
import pandas as pd
import random as r

BACKGROUND_COLOR = "#B1DDC6"
data = pd.read_csv("Intermediate/Day 31 Flash Cards/data/french_words.csv")
dict = data.to_dict(orient="records")
selection = {}
flip_timer = None

#-------------------------------------------IS KNOWN--------------------------------------------------------#
def is_known():
    dict.remove(selection)
    next_card()
    learn_data = pd.DataFrame(dict)
    learn_data.to_csv("Intermediate/Day 31 Flash Cards/data/french_words_to_learn.csv")
    
#-------------------------------------------FLIP CARD--------------------------------------------------------#
def flip_card():
    canvas.itemconfigure(card_background, image = back_img)
    canvas.itemconfigure(language, text="English", fill = "white")
    canvas.itemconfigure(word, text=selection["English"], fill = "white")
#-------------------------------------------NEXT CARD--------------------------------------------------------#
def next_card():
    global selection, flip_timer
    window.after_cancel(flip_timer)
    selection = r.choice(dict)
    canvas.itemconfigure(language, text="French", fill = "black")
    canvas.itemconfigure(word, text=selection["French"], fill = "black")
    canvas.itemconfigure(card_background, image = img)
    flip_timer= window.after(3000, flip_card)


#-------------------------------------------UI DESIGN--------------------------------------------------------#
#Creating Image and the Window
window = Tk()
window.title("Flashy")
window.config(padx = 50, pady = 50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img= PhotoImage(file="Intermediate/Day 31 Flash Cards/images/card_front.png")
back_img = PhotoImage(file="Intermediate/Day 31 Flash Cards/images/card_back.png")
card_background = canvas.create_image(400, 263, image=img)
language = canvas.create_text(400, 150, font=("Arial", 40, "italic")) 
word = canvas.create_text(400, 263, font=("Arial", 40, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

#Creating Buttons
incorrect_img = PhotoImage(file="Intermediate/Day 31 Flash Cards/images/wrong.png")
incorrect_button = Button(image=incorrect_img, command=next_card)
incorrect_button.grid(row=1, column=0)
correct_img = PhotoImage(file="Intermediate/Day 31 Flash Cards/images/right.png")
correct_button = Button(image=correct_img, command=is_known)
correct_button.grid(row=1, column=1)


next_card()

window.mainloop()
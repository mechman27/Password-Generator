from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip as ppc


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    if password_text.get() == "":
  
        #Create the password
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        pass_letters = [choice(letters) for _ in range(randint(8, 10))]
        pass_numbers = [choice(numbers) for _ in range(randint(3, 5))]
        pass_symbols = [choice(symbols) for _ in range(randint(3, 5))]
        alphabet = pass_letters + pass_numbers + pass_symbols
        shuffle(alphabet)
        #Add the password to the password text box using the secrets method instead of random
        password = "".join(alphabet)
        password_text.insert(0, password)
        ppc.copy(password)
    else:
        password_text.delete(0, END)
        #Create the password
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        pass_letters = [choice(letters) for _ in range(randint(8, 10))]
        pass_numbers = [choice(numbers) for _ in range(randint(3, 5))]
        pass_symbols = [choice(symbols) for _ in range(randint(3, 5))]
        alphabet = pass_letters + pass_numbers + pass_symbols
        shuffle(alphabet)
        #Add the password to the password text box using the secrets method instead of random
        password = "".join(alphabet)
        password_text.insert(0, password)
        ppc.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if website_text.get() != "" or password_text.get() != "":
        message_choice = messagebox.askokcancel(title="Password Prompt", message=f"These are the details entered: \nEmail: {email_text.get()} \nPassword: {password_text.get()}\n Website: {website_text.get()} \n If this is correct, click OK")
        if message_choice == True:
            with open("Intermediate/Day 29 Password Manager/data.txt", "a") as file:
                file.write(f"{website_text.get()}|{email_text.get()}|{password_text.get()}\n")
            website_text.delete(0, END)
            email_text.delete(0, END)
            email_text.insert(0, "example@email.com")
            password_text.delete(0, END)
    else: 
        messagebox.showerror(title="Password Prompt", message=f"There is a blank field, please try again")
        
# ---------------------------- UI SETUP ------------------------------- #

#create and implement tkinter window and the Canvas
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
IMG = PhotoImage(file="Intermediate/Day 29 Password Manager/logo.png")
canvas.create_image(100, 100, image=IMG)
canvas.grid(row=0, column=1)

#Create and implement tkinter labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

#Create and implement tkinter entry boxes
website_text = Entry(width=38)
website_text.grid(row=1, column=1, columnspan=2)
website_text.focus()
email_text = Entry(width=38)
email_text.grid(row=2, column=1, columnspan=2)
email_text.insert(0, "example@email.com")
password_text = Entry(width=21)
password_text.grid(row=3, column=1)

#Create and implement tkinter buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(width=36, text="Save Password", command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
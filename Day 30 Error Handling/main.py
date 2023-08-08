from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip as ppc
import json

#------------------------------ SEARCH FUNCTION ------------------------------- #
def search():
    try: 
        with open("Intermediate/Day 30 Error Handling/data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="File not found")
    else:
        if website_text.get() in data:
            messagebox.showinfo(title=website_text.get(), message=f"Email: {data[website_text.get()]['Email']}\nPassword: {data[website_text.get()]['Password']}")
        else:
            messagebox.showinfo(title="Error", message=f"no details for {website_text.get()}")


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
    new_data = {
        website_text.get(): {
            "Email": email_text.get(),
            "Password": password_text.get()
        }
    }
    if website_text.get() == "" or password_text.get() == "":
        messagebox.showerror(title="Password Prompt", message=f"There is a blank field, please try again")
    else: 
        try: 
            with open("Intermediate/Day 30 Error Handling/data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("Intermediate/Day 30 Error Handling/data.json", "w") as file:
                json.dump(data, file, indent=4)
        else:
            data.update(new_data)
            with open("Intermediate/Day 30 Error Handling/data.json", "w") as file:
                    json.dump(data, file, indent=4)
        finally:
            website_text.delete(0, END)
            password_text.delete(0, END)
            
        
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
website_text = Entry(width=21)
website_text.grid(row=1, column=1)
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
password_button = Button(text="Search", command=search, width=12)
password_button.grid(row=1, column=2)


window.mainloop()
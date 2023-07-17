import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

full_Pass = []
total_Char = nr_letters + nr_numbers + nr_symbols
letter_count = 0
number_count = 0
symbol_count = 0

for n in range(0, total_Char-1):
    random_choice = 0 
    random_choice = random.randint(0,2)
    if letter_count < nr_letters and random_choice == 0:
        letter_count += 1
        full_Pass.append(random.choice(letters))
    elif number_count < nr_numbers and random_choice == 1:
        number_count += 1
        full_Pass.append(random.choice(numbers))
    elif symbol_count < nr_symbols and random_choice == 2:
        symbol_count += 1
        full_Pass.append(random.choice(symbols))

password = ""
for n in full_Pass:
    password += n

print(f"Your password is: {password}")

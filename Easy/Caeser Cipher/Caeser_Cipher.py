from Caeser_Art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
done = False
def caesar(plain_text, shift_amount, directions):
            cipher_text = ""
            if directions == "decode":
                shift_amount *= -1
            for i in text:
                if i in alphabet:
                    position = alphabet.index(i)
                    new_position = position + shift_amount
                    new_letter = alphabet[new_position]
                    cipher_text += new_letter
                else:
                    cipher_text += i
            print(f"The {directions}d text is {cipher_text}")

while not done:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26
    caesar(plain_text=text, shift_amount=shift, directions=direction)

    choice = input("Would you like to restart? y for yes and n for no: \n").lower()
    if choice == "n" :
         done = True
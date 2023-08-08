import random
from Hangman_Art import logo
from Hangman_Art import stages
from Hangman_Words import word_list

#Variables
display = []
previous_letter = []
done = False
chosen_Word = random.choice(word_list)
word_length = len(chosen_Word)
lives = 6

#Create Blanks ("_")
for _ in range(word_length):
    display += "_"
print(logo)

#Playing the game
while not done:
    guess = input("Guess a Letter: ").lower()
    if guess in previous_letter:
        print(f"You've already guessed the letter {guess}. Please try again.")
    else:
        for position in range(word_length):
            letter = chosen_Word[position]
            if guess == letter:
                display[position] = guess
        previous_letter.append(guess)
              

        if guess not in chosen_Word:
            lives -= 1
        print(stages[lives])
        print(display)
        if "_" not in display:
            print("You Win")
            done = True
        if lives == 0: 
            print("You Lose")             
            print(f"The word was: {chosen_Word}")
            done = True
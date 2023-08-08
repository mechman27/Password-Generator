import random
from art import logo
attempts = 0 
answer = random.randint(1, 101)

    
def game(attempt_amount, final_answer):
    """Takes the random answer and number of attempts and plays a guessing game with user."""
    game_done = False
    while not game_done:
        guess = int(input(f"You have {attempt_amount} attempts remaining to guess the number.\nMake a guess: "))
        if guess > final_answer:
            print("Too high.")
            attempt_amount -= 1
        elif guess < final_answer:
            print("Too low.")
            attempt_amount -= 1
        else:
            print(f"You got it! the answer was {final_answer}.")
            game_done = True

        if attempt_amount != 0 and game_done != True:
            print("Guess again.")
        elif attempt_amount == 0:
            print("You've run out of guesses, you lose.")
            game_done = True
def turns(choice_str):
    if choice_str == "easy":
        return 10
    elif choice_str == "hard":
        return 5


print(logo)
choice = input("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100\nChoose a difficulty: type 'easy' or 'hard':")
attempts = turns(choice)
print(f"Psst, the answer is {answer}")
game(attempts, answer)
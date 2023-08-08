from gamedata import data
from art import logo, vs
import random
import os


def count(Computer_choiceA, Computer_choiceB ):
    """Returns the number of followers for each randomly chosen user"""
    if Computer_choiceA['follower_count'] > Computer_choiceB['follower_count']:
        return 'A'
    else:
        return 'B'

def grab_random():
    """Grabs a random choice from the gamedata.py file"""
    return random.choice(data)

def game():
    choiceA = grab_random()
    choiceB = grab_random()
    if choiceA == choiceB:
        choiceB = grab_random()
        print("This is a new selection")
    score = 0 
    game_done = False
   
    while not game_done: 
        print(f"Compare A: {choiceA['name']}, a(n) {choiceA['description']}, from {choiceA['country']}")
        print(vs)
        print(f"Against B: {choiceB['name']}, a(n) {choiceB['description']}, from {choiceB['country']}")
        answer = count(choiceA, choiceB)

        # Here for testing and debugging
        # print(answer)
        user_choice = input("Who has more follower? Type 'A' or 'B'").upper()

        os.system('clear')
        print(logo)
        if user_choice == answer:
            score += 1
            print(f"You're right. Current Score: {score}")
            choiceA = choiceB
            choiceB = random.choice(data)
        elif user_choice != answer:
            game_done = True
            print(f"Sorry, that's wrong. Final Score: {score}")
print(logo)        
game()
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
from art import logo
import os


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"


def BlackJack ():
    players_hand = []
    computers_hand = []

    for _ in range(2):
        players_hand.append(deal_card())
        computers_hand.append(deal_card())
    player_score = calculate_score(players_hand)
    computer_score = calculate_score(computers_hand)

    print(f"Your cards: {players_hand} Current Score: {player_score}")
    print(f"Computer's first card: {computers_hand[0]}")

    user_is_finished = False
    while not user_is_finished:
        
        if player_score == 0 or computer_score == 0 or player_score > 21:
            user_is_finished = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
               players_hand.append(deal_card())
               player_score = calculate_score(players_hand)
               print(f"Your cards: {players_hand} Current Score: {player_score}")
            else:
               user_is_finished = True
    
    while computer_score != 0 and computer_score < 18:
          computers_hand.append(deal_card())
          computer_score = calculate_score(computers_hand)
    print(f"Final hand: {players_hand}, final score: {player_score}")
    print(f"Computer's Final hand: {computers_hand}, Final Score: {computer_score}")
    print(compare(player_score, computer_score))
        
while input("Would you like to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    os.system("clear")
    print(logo)
    BlackJack()

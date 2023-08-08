from art import logo
import os
print(logo)
bidding_names = {}
done = False


while not done:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    stop = input("Is there anyone else that would like to bid? y for yes, n for no: \n").lower()
    bidding_names[name] = bid
    
    if stop == "n":
        done = True
    else:
        os.system('clear')

def highest_bidder(record):
    highest_bid = 0 
    winner = ""
    for value in record:
        bid_amount = record[value]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = value

    print(f"The Highest Bidder is: {winner} at ${highest_bid}")
    
highest_bidder(bidding_names)
from replit import clear

import art

print(art.logo)


def bid(player_name, player_bid):
    print("Welcome to Mystery Bid Master! Good luck!")
    player_name = input("What's your name?\n")
    player_bid = int(input("What's your bid? PLN"))
    bid_list[player_name] = player_bid

    while True:
        player = input("Are they any other users? Insert yes or no?")
        clear()
        if player == "no":
            player = "no"
            break
        elif player == "yes":
            player_name = input("What's your name?\n")
            player_bid = int(input("What's your bid? PLN"))
            bid_list[player_name] = player_bid

    max_value = max(bid_list.values())
    max_bidder = [name for name, bid in bid_list.items() if bid == max_value][0]
    print(f"{max_bidder} has the highest bid - {max_value} ")
    print("Thank you for playing")


player_name = ""
player_bid = 0
bid_list = {}

bid(player_name, player_bid)

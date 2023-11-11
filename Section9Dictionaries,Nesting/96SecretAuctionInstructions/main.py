import os
import art


anotherBidder = "yes"
bidders = []
print(art.logo)
print("Welcome to the secret auction program")
while anotherBidder == "yes":
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders.append({
        "name": name,
        "bid": bid
    })
    anotherBidder = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    

if anotherBidder == "no":
    largest_bid = {
        "bid": -1
    }
    for bid in bidders:
        if bid["bid"] > largest_bid["bid"]:
            largest_bid["bid"] = bid["bid"]
            largest_bid["name"] = bid["name"]
    print(f"The winner is {largest_bid["name"]} with a bid of ${largest_bid["bid"]}.")
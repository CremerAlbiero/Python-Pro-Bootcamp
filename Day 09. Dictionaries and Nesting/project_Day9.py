import os
all_bids = {}
names = True

print("Welcome to the secret auction program.")

while names:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    all_bids[name] = bid

    others = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if others == "no":
        break
    elif others != 'yes':
        print("Invalid input.")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

max_bidder = max(all_bids, key=all_bids.get)
max_bid = all_bids[max_bidder]

all_bids = {}
more_names = True
print("Welcome to the secret auction program.")


print(f"The winner is {max_bidder} with a bid of ${max_bid}.")
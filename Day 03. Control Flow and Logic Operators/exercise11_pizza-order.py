print("Thank you for choosing pyPizza Deliveries!")
size = input("Which size do you want? S, M or L\n") 
add_pepperoni = input("Do you wanna add pepperoni? Type 'Y' or 'N'\n") 
extra_cheese = input("Do you wanna extra cheese? Type 'Y' or 'N'\n") 
# Write your code below this line 
size, add_pepperoni, extra_cheese = size.lower(), add_pepperoni.lower(), extra_cheese.lower()
bill = 0

if add_pepperoni == 'y':
    add_pepperoni = True
elif add_pepperoni == 'n':
    add_pepperoni = False
else:
    add_pepperoni = False
    print("In pepperoni, you have to type Y or N. We'll consider N.\n")

if extra_cheese == 'y':
    extra_cheese = True
elif extra_cheese == 'n':
    extra_cheese = False
else:
    extra_cheese = False
    print("In extra cheese, you have to type Y or N. We'll consider N.\n")

if size == "s":
    bill += 15
    if add_pepperoni:
        bill += 2
    if extra_cheese:
        bill += 1
elif size == 'm':
    bill += 20
    if add_pepperoni:
        bill += 3
    if extra_cheese:
        bill += 1
elif size == 'l':
    bill += 25
    if add_pepperoni:
        bill += 3
    if extra_cheese:
        bill += 1
else:
    print("You typed the size incorrectly. Try again.")
print(f"Your final bill: ${bill}.")
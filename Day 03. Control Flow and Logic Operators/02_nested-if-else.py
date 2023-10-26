# Nested if else. 

print("Welcome to the Rollercoaster!")
height = int(input("What's your height in cm?\n"))
ticket = 0

if height >= 120:
    print("You can ride rollercoaster!")
    age = int(input("What's your age?\n"))
    if age < 12:
        ticket = 5
    elif age <= 18:
        ticket = 7
    else:
        ticket = 12
    print(f"You'll pay ${ticket} for the ticket.")
else:
    print("You can't ride.")
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
    #checking multiple conditions
    elif age >= 45 and age <= 55:
        print("Everything is gogin to be ok. Have a free ride on us!")
    else:
        ticket = 12
    print(f"You'll pay ${ticket} for the ticket.")

    wants_photo = input("Do you want a photo taken? Type 'Y' or 'N': ")
    wants_photo = wants_photo.lower()
    if wants_photo == "y":
        ticket += 3
    elif wants_photo == "yes":
        ticket += 3
    print(f"Your final bill will be: ${ticket}")
else:
    print("You can't ride.")
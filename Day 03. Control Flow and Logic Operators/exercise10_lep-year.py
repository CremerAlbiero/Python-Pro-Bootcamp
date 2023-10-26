year = int(input("Insert an year (example: 2000): "))
leap = True

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
        else:
            leap = False
    else:
        leap = True
else:
    leap = False

if leap:
    print(f"{year} it's a leap year.")
else:
    print(f"{year} it's not a leap year.")

#leap year verifier.
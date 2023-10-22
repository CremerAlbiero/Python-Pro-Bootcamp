print("Welcome to the tio calculator")
bill = float(input("What's the total bill ?\n$"))
perc = float(input("What percentage tip would you like to give? 10, 12, or 15?\n")) / 100
qty = int(input("How many people to split the bill?\n"))
result = round((bill * (1 + perc)) / qty, 2)
print(f"Each person should pay: ${result}")

#I used round(result_calculation, 2) to show only 2 number in the floating.point ($25.50).
target = int(input("Enter a number between 0 and 1000\n"))
# Do not change the code above

# Write your code here
even_sum = 0
for number in range(1, (target + 1)):
    if number % 2 == 0:
        even_sum += number
print(f"The total is: {even_sum}")

#I have to use the "target" + 1 because the range will stop just before the end.
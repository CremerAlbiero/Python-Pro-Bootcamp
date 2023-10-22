age = input("What's your age?\n")
# Don't change the code above

# Write your code below this line (assume that the person will live until 90 years old)
age = int(age)
weeks_total = 90 * 52     #the are 52 weeks in a year.
weeks_age = age * 52
x = weeks_total - weeks_age

print(f"You have {x} weeks left.")
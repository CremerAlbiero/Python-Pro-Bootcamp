# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above

# Write your code below this line (Body mass Index).
height = float(height)
weight = float(weight)

bmi = int(weight / (height ** 2))
print(f"Your BMI is {bmi}")
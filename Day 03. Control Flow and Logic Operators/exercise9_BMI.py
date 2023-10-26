#Improved BMI calculator

weight = float(input("What's your weight in kg (example: 72.5)?\n"))
height = float(input("What's your height in meters?(example: 1.65)\n"))

bmi = weight / (height**2)

if bmi < 19:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 40:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
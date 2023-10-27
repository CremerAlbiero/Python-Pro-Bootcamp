#program that calculates the average student height from a List of Heights. total of 7 students
# Input a Python list of student heights
student_heights = input("Insert all the students heights (example: 170, 158, 182...)\n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height = 0
number_students = 0
for h in student_heights:
  total_height += h
  number_students += 1
average_height = int(round(total_height / number_students))

print(f"total height = {total_height}")
print(f"number of students = {number_students}")
print(f"average height = {average_height}")

#I used round to floating-point number >= 0.5
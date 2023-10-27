# Input a list of student scores
student_scores = input("Student scores: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# create a code that could do the same as the max() function.
max = 0
for i in student_scores:
  if i > max:
    max = i
print(f"Highest score in the class: {max}")
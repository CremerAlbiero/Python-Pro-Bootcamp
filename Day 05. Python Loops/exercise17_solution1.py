# Input a list of student scores
student_scores = input("Student scores: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# create a code that could do the same as the max() function.
student_scores.sort()
student_scores.reverse()
max = student_scores
print(f"The highest score in the class is: {max[0]}")
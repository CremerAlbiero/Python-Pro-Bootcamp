print("The Love Calculator is calculating your score...")
name1 = input("What's you name?\n") # What is your name?
name2 = input("What's their name?\n") # What is their name?
# Don't change the code above
# Write your code below this line
both_names = name1.lower() + name2.lower()
print(both_names)

t = both_names.count('t')
r = both_names.count('r')
u = both_names.count('u')
e = both_names.count('e')
true_score = t + r + u + e
print(true_score)

l = both_names.count('l')
o = both_names.count('o')
v = both_names.count('v')
e = both_names.count('e')
love_score = l + o + v + e
print(love_score)



total = int(str(true_score) + str(love_score))


if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like peanut butter and jelly.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
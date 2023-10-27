# Write your code below this line
# Hint: Remember to import the random module first. 🎲
from random import randint
coin = randint(0, 1)
if coin == 0:
    print("Tails")
else:
    print("Heads")
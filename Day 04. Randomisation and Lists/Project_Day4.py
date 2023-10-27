from random import randint
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

games = [rock, paper, scissors]
plays = [0, 1, 2]
computer = randint(0, 2)
player_choice = int(input("What will you go? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


if player_choice in plays:
    print(f"Your play:\n")
    print(games[player_choice])

if computer in plays:
    print(f"Computer:\n")
    print(games[computer])

else:
    print("Invalid Input. Please type just 0, 1 or 2.")

if player_choice == 0 and computer == 2:
    winner = True
elif player_choice == 1 and computer == 0:
        winner = True
elif player_choice == 2 and computer == 1:
    winner = True
elif player_choice == computer:
    winner = True
else:
    winner = False

if winner and not player_choice == computer:
    print("You won")
elif player_choice == computer:
    print("Draw")
else:
    print("You lose")
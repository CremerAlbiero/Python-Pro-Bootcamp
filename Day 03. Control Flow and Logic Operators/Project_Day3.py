print("Welcome to Treasure Island.\nYour Mission is to find the treasure.")
choice1 = input("You find yourself at a crossroad. Do you want to go 'left' or 'right'?\n").lower()

if choice1 == "left":
    choice2 = input("You see a lake. Would you like to 'swim' or 'wait'?\n").lower()
    if choice2 == 'wait':
        print("You waited for a while and saw a what seems like an entrance for a cavern or something. When you approached, you saw three doors.")
        choice3 = input("They're red, blue and yellow. Which one do you choose?\n").lower()
        if choice3 == "yellow":
            print("You won! Congratulations!")
            game_over = False
        elif choice3 == 'red':
            print("You've been burned alive!")
            game_over = True
        else:
            print("You've been eaten by beats!")
            game_over = True
    else:
        print("You've been attacked by a shark.")
        game_over = True
else:
    print("You fell into a hole.")
    game_over = True
    
if game_over:
    print("Game Over.")
else:
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
      ''')   #src: https://ascii.co.uk/art
from random import choice
from words_lists import *

categories = [soccer_teams, holidays, professions, sports, weather, planets, countries, fruits, animals]
selected_words = []

# choosing randomly an word from "words_list.py".
for category in categories:
    random_words = choice(category)
    selected_words.append(random_words)
word_selected = choice(selected_words)
word_lenght = len(word_selected)


# putting all the letters in word_selected inside a list.
word_game = []
for letters in word_selected:
    word_game.append(letters)

display_game = []
for letter in word_selected:
    display_game.append(" _ ")

# user attempts
user_attempts = 7
if word_lenght >= 7:
    user_attempts = word_lenght + 2 
print(f"The word has {word_lenght} letters.\nYou'll have {user_attempts} attempts in total.")
print(display_game)

guessed_letters = []

while word_game != display_game and user_attempts > 0:
    user_guess = input("Guess a letter: ").lower()

    if user_guess in guessed_letters:
        print("You've already guessed that letter")
        user_attempts -= 1
        print(f"{user_attempts} attemps left.")
        continue

    guessed_letters.append(user_guess)

    if user_guess in word_game:
        for i in range(word_lenght):
            letter = word_game[i]
            if user_guess == letter:
                display_game[i] = letter
        print(" ".join(display_game))
    else:
        user_attempts -= 1
        print(f"Wrong. You have {user_attempts} attempts left.")
        print(" ".join(display_game))

if word_game == display_game:
    print("You won!")
else:
    print("Game over.")
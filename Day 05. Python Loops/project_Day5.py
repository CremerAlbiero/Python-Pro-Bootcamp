from random import choice, shuffle

letters_list = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', ':', ';', '<', '>', '?', '/', '.', ',']
print("Welcome to the Password Generator!")
qty_letter = int(input("How many letters do you want?\n"))
qty_number = int(input("How many numbers do you want?\n"))
qty_symbol = int(input("How many symbols do you want it to have?\n"))

password_elements = []
for _ in range(qty_letter):
    letter = choice(letters_list)
    password_elements.append(letter)

for _ in range(qty_number):
    number = choice(numbers_list)
    password_elements.append(number)

for _ in range(qty_symbol):
    symbol = choice(symbols_list)
    password_elements.append(symbol)

# I used shuffle() to rearrange randomly all the elements.
shuffle(password_elements)
final_password = ' '.join(password_elements)
print("Make sure to write it down offline. Below it's your password.")
print(final_password)
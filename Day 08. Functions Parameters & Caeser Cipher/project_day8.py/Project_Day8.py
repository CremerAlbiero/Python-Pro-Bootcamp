alphabet = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
while direction not in ["encode", "decode"]:
    print("Invalid input, type just encode or decode.")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message:\n").lower()

shift = int(input("Type the shift number:\n"))
while shift < 1 or shift > 26:
    print("This number is invalid. Insert between 1 and 26.")
    shift = int(input("Type the shift number:\n"))

def caesar(crypted_txt, shift_number, direction_name):
    crypted_txt = []
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                crypted_txt.append(alphabet[position + shift_number])
                direction_name = "encrypted"
            elif direction == "decode":
                crypted_txt.append(alphabet[position - shift_number])
                direction_name = "decrypted"
        else:
            crypted_txt.append(letter)

    crypted_msg = ''.join(crypted_txt)
    print(f"The {direction_name} message is {crypted_msg}")


caesar(crypted_txt=text, shift_number=shift, direction_name=direction)
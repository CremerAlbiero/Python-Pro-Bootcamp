alphabet = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(encrypted_txt, shift_number):
    encrypted_txt = []
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            encrypted_txt.append(alphabet[position + shift_number])
    encoded_msg = ''.join(encrypted_txt)
    print(f"The encoded message is {encoded_msg}")

encrypt(encrypted_txt=text, shift_number=shift)

# note: the join method it's used to concatenate a list of strings into a single string.
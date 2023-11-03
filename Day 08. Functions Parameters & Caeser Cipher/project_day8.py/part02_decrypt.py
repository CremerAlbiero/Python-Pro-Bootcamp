alphabet = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# create decrypt function
def decrypt(decrypted_txt, shift_number):
    decrypted_txt = []
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            decrypted_txt.append(alphabet[position - shift_number])
    decoded_msg = ''.join(decrypted_txt)
    print(f"The decrypted message is {decoded_msg}")
decrypt(decrypted_txt=text, shift_number=shift)
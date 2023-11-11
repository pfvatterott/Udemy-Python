import alphabet


def encrypt(text, shift):
    encryptedText = ""
    for letter in text:
        index = alphabet.alphabet.index(letter)
        shiftIndex = index + shift
        if (shiftIndex > len(alphabet.alphabet) - 1):
            shiftIndex = shiftIndex - len(alphabet.alphabet)
        encryptedText += alphabet.alphabet[shiftIndex]
    print(encryptedText)
    

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypt(text, shift)


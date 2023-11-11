import alphabet
import art

def encrypt(text, shift):
    encryptedText = ""
    for letter in text:
        index = alphabet.alphabet.index(letter)
        shiftIndex = index + shift
        if (shiftIndex > len(alphabet.alphabet) - 1):
            shiftIndex = shiftIndex - len(alphabet.alphabet)
        encryptedText += alphabet.alphabet[shiftIndex]
    print(encryptedText)
    
def decrypt(text, shift):
    decryptedText = ""
    for letter in text:
        index = alphabet.alphabet.index(letter)
        shiftIndex = index - shift
        if (shiftIndex < 0):
            shiftIndex = len(alphabet.alphabet) + shiftIndex
        decryptedText += alphabet.alphabet[shiftIndex]
    print(decryptedText)
    
print(art.logo)
isPlaying = 'yes'
while isPlaying == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)
    isPlaying = input("Would you like to keep playing? Type yes or no.").lower()


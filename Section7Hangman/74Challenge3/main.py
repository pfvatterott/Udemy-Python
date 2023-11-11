import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display.append("_")

while "_" in display:
    print(display)
    guess = input("Guess a letter\n").lower()
    index = 0
    for letter in chosen_word:
        if guess == letter:
            display[index] = guess
        else:
            print("Wrong")
        index += 1

print("You win!")
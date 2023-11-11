import random
word_list = ["ardvark", "baboon", "camel"]

chosen_word = word_list[random.randint(0, len(word_list) - 1)]
chosen_word_array = []
for letter in range(len(chosen_word)):
    chosen_word_array.append(chosen_word[letter])
print(chosen_word_array)
guess = input("Guess a letter\n").lower()

for letter in chosen_word_array:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")
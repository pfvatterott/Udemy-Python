import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

guesses_left = 6
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display.append("_")

while "_" in display and guesses_left > 0:
    print(display)
    print(stages[guesses_left])
    guess = input("Guess a letter\n").lower()
    index = 0
    isCorrect = False
    for letter in chosen_word:
        if guess == letter:
            display[index] = guess
            isCorrect = True            
        index += 1
    if isCorrect == False:
        guesses_left -= 1
        if guesses_left == 0:
            print(display)
            print(stages[guesses_left])
            print("LOSER")

if "_" not in display:
    print("You win!")
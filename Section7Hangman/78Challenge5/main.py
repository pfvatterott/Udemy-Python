import random
import hangman_art
import hangman_words

guesses_left = 6
chosen_word = random.choice(hangman_words.word_list)
print(hangman_art.logo)
display = []
for letter in chosen_word:
    display.append("_")

while "_" in display and guesses_left > 0:
    print(display)
    print(hangman_art.stages[guesses_left])
    guess = input("Guess a letter\n").lower()
    index = 0
    isCorrect = False
    guessedBefore = False
    for letter in chosen_word:
        if guess in display:
            guessedBefore = True
        if guess == letter:
            display[index] = guess
            isCorrect = True            
        index += 1
    if guessedBefore == True:
        print("You've already guessed that, silly!")
    if isCorrect == False:
        guesses_left -= 1
        if guesses_left == 0:
            print(display)
            print(hangman_art.stages[guesses_left])
            print("LOSER")

if "_" not in display:
    print("You win!")
import art
import random


def generate_random_number():
    return random.randint(1, 100)

def check_guess(user_guess, correct_number):
    if user_guess > correct_number:
        return "Too high!"
    elif user_guess < correct_number:
        return "Too low!"
    else:
        return "You got it!"

def guess_the_number():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    easy_or_hard = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if easy_or_hard == "easy":
        guesses_remaining = 10
    else: 
        guesses_remaining = 5
    correct_number = generate_random_number()
    while guesses_remaining > 0:
        print(f"You have {guesses_remaining} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        check_guess_result = check_guess(user_guess, correct_number)
        if check_guess_result == "You got it!":
            print(f"{check_guess_result} The answer was {correct_number}.")
            guesses_remaining = 0
        else:
            print(check_guess_result)
            guesses_remaining -= 1
            if guesses_remaining > 0:
                print("Guess again.")
    if (guesses_remaining == 0):
        print(f"LOSER! The correct number was {correct_number}")
        
    
guess_the_number()
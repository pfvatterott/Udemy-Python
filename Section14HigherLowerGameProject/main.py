import art
import game_data
import random
import os

def get_random_data():
    random_index = random.randint(0, len(game_data.data) - 1)
    random_data_to_return = game_data.data[random_index]
    del game_data.data[random_index]
    return random_data_to_return

def check_answer(answer, a_data, b_data):
    if answer == 'a' and a_data > b_data:
        return True
    elif answer == 'b' and b_data > a_data:
        return True
    else:
        return False
    
def display_loss_game(score):
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    
def display_win_game(score):
    print(art.logo)
    print(f"Wow, that was impressive! We're all out of data to use. Final score: {score}")
               

def higher_or_lower():
    score = 0
    compare_A = get_random_data()
    compare_B = get_random_data()
    is_correct = True
    
    while is_correct:
        print(art.logo)
        if score > 0:
            print(f"You're right! Current score: {score}")
        print(f"Compare A: {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}.")
        print(art.vs)
        print(f"Compare B: {compare_B['name']}, a {compare_B['description']}, from {compare_B['country']}.")
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = check_answer(answer, compare_A['follower_count'], compare_B['follower_count'])
        os.system('cls' if os.name == 'nt' else 'clear')
        if is_correct:
            score += 1
            if len(game_data.data) == 0:
                display_win_game(score)
            else:
                compare_A = compare_B
                compare_B = get_random_data()
        else:
            display_loss_game(score)
            
        
    
    
    
higher_or_lower()
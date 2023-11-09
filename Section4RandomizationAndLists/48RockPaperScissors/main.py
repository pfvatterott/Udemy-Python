import random

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)

if player_choice == computer_choice:
    print("Tied game! Play again.")
    
if player_choice == 0 and computer_choice == 1:
    print("Computer chose paper, you lose")
elif player_choice == 0 and computer_choice == 2:
    print("Computer chose scissors, You win!") 
elif player_choice == 1 and computer_choice == 2:
    print("Computer chose scissors, You lose")
elif player_choice == 1 and computer_choice == 0:
    print("Computer chose rock,You win!")
elif player_choice == 2 and computer_choice == 0:
    print("Computer chose rock, You lose")
elif player_choice == 1 and computer_choice == 1:
    print("Computer chose paper, You win!")
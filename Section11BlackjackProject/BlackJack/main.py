import art
import random


def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return cards[random.randint(0, len(cards) - 1)]

def begin_game(): 
    cards_in_play = {
        "dealer": [draw_card(), draw_card()],
        "player": [draw_card(), draw_card()]
    }
    return cards_in_play
    
def find_total_score(cards):
    total = 0
    for card in cards:
        total += card
    return total

def find_total_score_when_ace(cards):
    total = 0
    for card in cards:
        if card == 11:
            total += 1
        else:
            total += card
    return total

def display_score(cards_in_play, player_score):
    print(f"Your cards: {cards_in_play["player"]}, current score: {player_score}")
    print(f"Dealer's first card: {cards_in_play["dealer"][0]}\n")
    
def display_score_end_game(cards_in_play, player_score, dealer_score):
    print(f"Your cards: {cards_in_play["player"]}, current score: {player_score}")
    print(f"Dealer's cards: {cards_in_play["dealer"]}, current score: {dealer_score}\n")
    
def dealer_end_game(cards_in_play, player_score, dealer_score):
    while dealer_score < 17:
        cards_in_play["dealer"].append(draw_card())
        dealer_score = find_total_score(cards_in_play["dealer"])
        display_score_end_game(cards_in_play, player_score, dealer_score)
        input("Press any button to continue")
        if dealer_score > 21:
            dealer_score = find_total_score_when_ace(cards_in_play["dealer"])
            if dealer_score > 21:
                return "Dealer busts!"
        elif dealer_score < 22 and dealer_score > player_score:
            return "Dealer wins!"
        elif dealer_score == 21:
            return "Dealer wins!"
    if dealer_score < player_score:
        return "Player wins!"
    elif dealer_score == player_score:
        return "Tie!"
    else:
        return "Dealer wins!"

def blackjack():
    print(art.logo)
    cards_in_play = begin_game()
    player_score = find_total_score(cards_in_play["player"])
    dealer_score = find_total_score(cards_in_play["dealer"])
    display_score(cards_in_play, player_score)

    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    while another_card == 'y':
        cards_in_play["player"].append(draw_card())
        player_score = find_total_score(cards_in_play["player"])
        display_score(cards_in_play, player_score)
        if player_score > 21:
            player_score = find_total_score_when_ace(cards_in_play["player"])
            if player_score > 21:
                print("Bust!")
                play_game = input("Do you want to play another round of Blackjack? Type 'y' or 'n': ")
                if play_game == 'y':
                    blackjack()
                else:
                    return
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if (another_card == 'n'):
        display_score_end_game(cards_in_play, player_score, dealer_score)
        input("Press any button to continue")
        print(dealer_end_game(cards_in_play, player_score, dealer_score))
        play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if play_game == 'y':
            blackjack()
    
    
    
    
play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play_game == 'y':
    blackjack()
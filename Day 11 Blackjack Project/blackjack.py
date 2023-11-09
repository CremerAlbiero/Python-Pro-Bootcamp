from random import randint, choice

dealer_points = 0
player_points = 0

# I'm considering 3 decks
decks = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 3

player_hand = []
dealer_hand = []

def start_card(player_hand):
    for _ in range(2):
        card = choice(decks)
        decks.remove(card)
        player_hand.append(card)
    return player_hand

def pick_1card():
    card = choice(decks)
    return card

def adjust_aces(hand):
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1

def display_hands():
    print("Dealer:", dealer_hand)
    print("Player:", player_hand)

def rounds():
    global dealer_points, player_points
    global player_hand, dealer_hand

    start_card(dealer_hand)
    start_card(player_hand)
    display_hands()

    while sum(player_hand) < 22:
        player_choice = input("Type 'hit' to get another card or 'stand' to end.\n").lower()

        if player_choice == 'hit':
            player_hand.append(pick_1card())
            adjust_aces(player_hand)
            display_hands()

        elif player_choice == 'stand':
            break

    while sum(dealer_hand) < 17:
        dealer_hand.append(pick_1card())
        adjust_aces(dealer_hand)
        print(f"Dealer's hand: {dealer_hand}")

    score_player, score_dealer = sum(player_hand), sum(dealer_hand)

    if score_player > 21:
        print("You went over 21...")
        dealer_points += 1

    elif score_dealer > 21:
        print("Dealer went over. You won.")
        player_points += 1

    elif score_player == 21:
        print("Blackjack! You won this round.")
        player_points += 1

    elif score_dealer == 21:
        print("Blackjack for dealer!")
        dealer_points += 1

    elif score_player > score_dealer:
        print("You won this round!")
        player_points += 1

    elif score_dealer > score_player:
        print("You lose.")
        dealer_points += 1

    elif score_player == score_dealer:
        print("Draw")

    print(f"\nPlayer total wins: {player_points}\nDealer: {dealer_points}\n")

while True:
    rounds()

    play_again = input("Do you want to play another round? (yes/no) ").lower()

    #bug fixed: players restart with the previous hand.
    player_hand = []
    dealer_hand = []
    if play_again != 'yes':
        break

print(f"Game Over.\nPlayer: {player_points}\nDealer: {dealer_points}")
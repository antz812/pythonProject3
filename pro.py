import random

# card values (including 10s)
card_values = {
    'Ace': 11,
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10,  # Note: In Spanish Blackjack, all 10s are included
    'Jack': 10, 'Queen': 10, 'King': 10
}

def deal_card():
    return random.choice(list(card_values.keys()))

def hand_value(hand):
    total = sum(card_values[card] for card in hand)
    # Adjust for Aces (if total > 21)
    if 'Ace' in hand and total > 21:
        total -= 10
    return total

def spanish_blackjack():
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    print(f"Player's hand: {player_hand}")
    print(f"Dealer's visible card: {dealer_hand[0]}")

    while True:
        action = input("Do you want to hit or stay? ").lower()
        if action == 'hit':
            player_hand.append(deal_card())
            print(f"Player's hand: {player_hand}")
            if hand_value(player_hand) > 21:
                print("Player busts! Dealer cheated to win.")
                break
        elif action == 'stay':
            while hand_value(dealer_hand) < 17:
                dealer_hand.append(deal_card())
            print(f"Dealer's hand: {dealer_hand}")
            if hand_value(dealer_hand) > 21:
                print("Dealer busts! Player wins.")
            elif hand_value(player_hand) > hand_value(dealer_hand):
                print("Player wins!")
            elif hand_value(player_hand) < hand_value(dealer_hand):
                print("Dealer cheated to win.")
            else:
                print("PUSH!")
            break
        else:
            print("Invalid input. Please enter 'hit' or 'stay'.")

spanish_blackjack()

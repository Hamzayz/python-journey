# DAY 11: BLACKJACK GAME PROJECT
# This project implements a simplified version of the Blackjack card game

# IMPORTING MODULES:
import random  # For random card selection

# GAME SETUP:
print("Welcome to the Blackjack!")

# CARD DEFINITIONS:
# List of card values (Ace can be 1 or 11)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

# Dictionary mapping card names to their values
cards_names = {
    "2 of Hearts": 2, "3 of Hearts": 3, "4 of Hearts": 4, "5 of Hearts": 5,
    "6 of Hearts": 6, "7 of Hearts": 7, "8 of Hearts": 8, "9 of Hearts": 9,
    "10 of Hearts": 10, "Jack of Hearts": 10, "Queen of Hearts": 10,
    "King of Hearts": 10, "Ace of Hearts": 11,
}

# MAIN GAME LOOP:
continues = True
while continues:
    # Initial Deal:
    # Deal two cards to user and calculate score
    user_cards = random.sample(cards, 2)  # random.sample ensures no duplicates
    user_score = sum(user_cards)
    print(f"Your cards: {user_cards}, score {user_score}")

    # Deal two cards to dealer and calculate score
    dealer_cards = random.sample(cards, 2)
    dealer_score = sum(dealer_cards)
    print(f"Dealer's first card: {dealer_cards[0]}")  # Show only first card

    # Dealer's Play:
    # Dealer must hit if score is less than 17
    if dealer_score < 17:
        dealer_card_3 = random.choice(cards)
        dealer_cards.append(dealer_card_3)
        dealer_score = sum(dealer_cards)

    # User's Turn:
    # Ask if user wants another card
    want_card = input("Type 'y' to get another card or type 'n' to pass:").lower()
    if want_card == "y":
        new_card = random.choice(cards)
        user_cards.append(new_card)
        user_score = sum(user_cards)

    # Ace Handling:
    # If score exceeds 21 and user has an Ace, convert it to 1
    if user_score > 21:
        if 11 in user_cards:
            index_11 = user_cards.index(11)
            user_cards[index_11] = 1
            user_score = sum(user_cards)

    # Automatic Hit:
    # If user's score is less than 17, automatically give another card
    if user_score < 17:
        user_card_3 = random.choice(cards)
        user_cards.append(user_card_3)
        user_score = sum(user_cards)

    # Show Final Results:
    print(f"Your final cards: {user_cards}, final score: {user_score}")
    print(f"Dealer final cards: {dealer_cards}, final score: {dealer_score}")

    # WINNING RULES:
    # 1. If user's score > 21: Bust (Dealer wins)
    # 2. If dealer's score > 21: Dealer busts (User wins)
    # 3. If user's score > dealer's score: User wins
    # 4. If dealer's score > user's score: Dealer wins
    # 5. If scores are equal: Draw
    if user_score > 21:
        print("You busted! Dealer wins!")
    elif dealer_score > 21:
        print("Dealer busted! You win!")
    elif user_score > dealer_score:
        print("You win!")
    elif dealer_score > user_score:
        print("Dealer wins!")
    elif user_score == dealer_score:
        print("It's Draw!")

    # Ask to play again
    play = input("If you want to play again type 'y' or type 'n': ")
    if play == "n":
        continues = False
        print("Bye")
import random

playerIn = True
dealerIn = True

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A',
         2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A',
         2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A',
         2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

playerHand = []
opponentHand = []

def deal(turn):
    card = random.choice(cards)
    turn.append(card)
    cards.remove(card)

def total(turn):
    total = 0
    picCard = ['J', 'Q', 'K']
    for card in turn:
        if card in range (1,11):
            total += card
        elif card in picCard:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total

def showOpponentHand():
    if len(opponentHand) == 2:
        return opponentHand[0]
    elif len(opponentHand) > 2:
        return opponentHand[0], opponentHand[1]

for i in range(2):
    deal(opponentHand)
    deal(playerHand)

while playerIn or dealerIn:
    print(f"Dealer had {showOpponentHand()} and X")
    print(f"You have {playerHand} for a total of {total(playerHand)}")
    if playerIn:
        anotherCard = input("1: Reveal\n2:Take another card\n")
    if total(opponentHand) > 16:
        dealerIn = False
    else:
        deal(opponentHand)
    if anotherCard == '1':
        playerIn = False
    else:
        deal(playerHand)
    if total(playerHand) >= 21:
        break
    elif total(opponentHand) >= 21:
        break

if total(playerHand) == 21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {opponentHand} for a total of {total(opponentHand)}")
    print("Blackjack! You win!")
elif total(opponentHand) == 21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {opponentHand} for a total of {total(opponentHand)}")
    print("Blackjack! Dealer wins!")
elif total(playerHand) > 21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {opponentHand} for a total of {total(opponentHand)}")
    print("You bust! Dealer wins!")
elif total(opponentHand) > 21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {opponentHand} for a total of {total(opponentHand)}")
    print("Dealer busts! You win!")
elif 21 - total(opponentHand) < 21 - total(playerHand):
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {opponentHand} for a total of {total(opponentHand)}")
    print("Dealer wins!")
elif 21 - total(opponentHand) > 21 - total(playerHand):
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {opponentHand} for a total of {total(opponentHand)}")
    print("You win!")

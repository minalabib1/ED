import random
playerIn = True
dealerIn = True

# deck of cards/ player dealer hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        'J', 'Q','K', 'A', 'J', 'Q','K', 'A', 'J', 'Q','K', 'A', 'J', 'Q','K', 'A']
playerHand = []
dealerHand = []

# deal the cards
def dealCard(turn):
    card = random.choice(deck) #select random card from deck
    turn.append(card)          # we add it to the Hand, player or dealer depending on whos turn it is
    deck.remove(card)          # then we remove that card from the deck so it doesnt get picked again


#cal total of each hand
def total(hand):
    total = 0
    aces = 0
    for card in hand:
        if card in range(2, 11):
            total += card
        elif card in ['J', 'K', 'Q']:
            total += 10
        else:
            total += 11
            aces += 1
    while aces and total > 21:
        total -= 10
        aces -= 1
    return total


#check who won!
def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]
        


# game loop

for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand)

print(dealerHand, "dealer")
print(playerHand, "player")

while playerIn or dealerIn:
    print(f"Dealer had {revealDealerHand()} and X")
    print(f"you have {playerHand} for a total of {total(playerHand)}")
    if playerIn:
        stayOrHit = input("1: Stay\n2: Hit\n")
    if total(dealerHand) > 16:
       dealerIn = False
    else:
        dealCard(dealerHand)
    if stayOrHit == '1':
        playerIn = False
    else:
        dealCard(playerHand)
    if total(playerHand) >= 21:
        break
    elif total(dealerHand) >= 21:
        break

if total(playerHand) == 21:
    print(f"\n U have {playerHand} for a total of {total(playerHand)} and dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("Blackjack! u win dawg")
elif total(dealerHand) == 21:
        print(f"\n U have {playerHand} for a total of {total(playerHand)} and dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Blackjack! Dealer Wins")
elif total(playerHand) > 21:
        print(f"\n U have {playerHand} for a total of {total(playerHand)} and dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("You Bust, dealer wins")
elif total(dealerHand) > 21:
        print(f"\n U have {playerHand} for a total of {total(playerHand)} and dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Dealer busted all over you, you win!")
elif 21 - total(dealerHand) < 21 - total(playerHand):
        print(f"\n U have {playerHand} for a total of {total(playerHand)} and dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Dealer wins")
elif 21 - total(dealerHand) > 21 - total(playerHand):
         print(f"\n U have {playerHand} for a total of {total(playerHand)} and dealer has {dealerHand} for a total of {total(dealerHand)}")
         print("you win")
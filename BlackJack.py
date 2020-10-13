import random as r

#Class for the cards attributes
class Card():
    def __init__(self,Suite,num,val):
        self.Suite = Suite
        self.num = num
        self.val=val

#Creating the deck
def createDeck():
    suites = ["Hearts", "Clubs", "Diamonds", "Spades"]
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cardsValues = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
    deck = []

    for suite in suites:
        for card in cards:
            deck.append(Card(suite,card,cardsValues[card]))

    return deck

#checking the deck values to make sure all the cards are there by values
def checkDeck(deck):
    for i in range(len(deck)):
        print(deck[i].val)

#Checking the hand value
def checkHandVal(hand):
    totalVal = 0
    for i in range(len(hand)):
        totalVal = totalVal + hand[i].val

    return totalVal

#Set the initial cards for the dealer and player
def drawFirstCards(playerHand,dealerHand,usedCards,deck):
    e = r.randint(0, 51)
    f = r.randint(0, 51)
    g = r.randint(0, 51)
    h = r.randint(0, 51)

    if deck[e] not in usedCards:
        usedCards.append(deck[e])
        playerHand.append(deck[e])
    if deck[g] not in usedCards:
        usedCards.append(deck[g])
        dealerHand.append(deck[g])
    if deck[f] not in usedCards:
        usedCards.append(deck[f])
        playerHand.append(deck[f])
    if deck[h] not in usedCards:
        usedCards.append(deck[h])
        dealerHand.append(deck[h])

    return playerHand,dealerHand,usedCards,deck

#the game
def BlackJack():
    #Player Hand, Dealer Hand,
    playerHand = []
    dealerHand = []
    usedCards = []
    deck = createDeck()
    drawFirstCards(playerHand, dealerHand, usedCards, deck)
    playerHandVal = checkHandVal(playerHand)
    dealerHandVal = checkHandVal(dealerHand)


    while playerHandVal < 21:
        for i in range(len(playerHand)):
            print(playerHand[i].num, " of ",playerHand[i].Suite)
        print("Player Hand Value: ", playerHandVal)
        choice = input("Would you like to hit? Y/N: ")
        if (choice == 'y' or choice == 'Y'):
            e = r.randint(0,51)
            if deck[e] not in usedCards:
                usedCards.append(deck[e])
                playerHand.append(deck[e])
                playerHandVal = checkHandVal(playerHand)
                for o in range(len(playerHand)):
                    if (playerHand[o].val == 11 and playerHandVal > 21):
                        playerHand[o].val = 1
                        playerHandVal = checkHandVal(playerHand)
        else:
            break

    while dealerHandVal < 21:
        for i in range(len(dealerHand)):
            print(dealerHand[i].num, " of ",dealerHand[i].Suite)
        print("Dealer Hand Value: ", dealerHandVal)
        if dealerHandVal <= 16:
            f = r.randint(0,51)
            if deck[f] not in usedCards:
                usedCards.append(deck[f])
                dealerHand.append(deck[f])
                dealerHandVal = checkHandVal(dealerHand)
                for o in range(len(dealerHand)):
                    if (dealerHand[o].val == 11 and dealerHandVal > 21):
                        dealerHand[o].val = 1
                        dealerHandVal = checkHandVal(dealerHand)
        else:
            break


    if (playerHandVal == 21 and len(playerHand) == 2):
        print("BlackJack!!!")
    elif dealerHandVal == playerHandVal:
        print("Pushed")
    elif dealerHandVal > playerHandVal or playerHandVal > 21:
        print("Dealer Wins")
    elif playerHandVal > dealerHandVal or dealerHandVal > 21:
        print("Player Wins")
BlackJack()






#deck = createDeck()
#checkDeck(deck)
#hand = [Card("hearts",10,10), Card("Spade",'A', 11)]
#total = checkHandVal(hand)
#print(total)
#drawFirstCards()
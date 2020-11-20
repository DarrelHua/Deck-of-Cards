from Deck_of_cards import Deck
from Deck_of_cards import Card


#First I need to create a deck and shuffle the cards

deck = Deck()
deck.shuffle()

#make the dealer and player
player = []
dealer = []

#Create the game of blackjack 
while len(player) < 2:
    player.append(deck.drawCard)

print(player)



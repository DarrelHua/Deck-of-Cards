import random

class Card:
    def __init__(self,val,suit):
        self.val = val
        self.suit = suit

    def show(self):
        print("{} of {}".format(self.val,self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.builds()

    def builds(self):
        suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        for i in suits:
            for j in range(1,14):
                self.cards.append(Card(j,i))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0,i)
            self.cards[i],self.cards[r] = self.cards[r], self.cards[i]

deck = Deck()
deck.shuffle()
deck.show()

class Player:
    def __init__(self):
        pass
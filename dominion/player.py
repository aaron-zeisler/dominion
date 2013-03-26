
from dominion.pile import Pile
from dominion.hand import Hand as HandClass
from dominion import dominion_rules

class Player(object):

    Name = None
    DrawPile = Pile()
    DiscardPile = Pile()
    Hand = HandClass()

    def __init__(self, name=None):
        self.Name = name
        self.DrawPile = Pile()
        self.DiscardPile = Pile()
        self.Hand = HandClass()

    def draw(self):
        #TODO: If the draw pile is empty, move the discard pile to the draw pile and shuffle
        drawnCard = self.DrawPile.draw()
        self.Hand.draw(drawnCard)

    def drawHand(self):
        for i in range(dominion_rules.HAND_SIZE):
            self.draw()

    def shuffle(self):
        self.DrawPile.shuffle()
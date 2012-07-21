
from dominion.pile import Pile
from dominion.hand import Hand as HandClass

class Player(object):

    DrawPile = Pile()
    DiscardPile = Pile()
    Hand = HandClass()

    def __init__(self):
        self.DrawPile = Pile()
        self.DiscardPile = Pile()
        self.Hand = HandClass()

    def draw(self):
        drawnCard = self.DrawPile.draw()
        self.Hand.draw(drawnCard)

    def shuffle(self):
        self.DrawPile.shuffle()
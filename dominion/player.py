
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
        if self.DrawPile.len() == 0:
            self.moveDiscardPileToDrawPile()

        drawnCard = self.DrawPile.draw()
        self.Hand.draw(drawnCard)
        return drawnCard

    def discard(self, card):
        self.DiscardPile.drop(self.Hand.discard(card))

    def drawHand(self):
        for i in range(dominion_rules.HAND_SIZE):
            self.draw()

    def discardHand(self):
        while self.Hand.len() > 0:
            card = self.Hand.Cards[0]
            self.discard(card)

    def shuffle(self):
        self.DrawPile.shuffle()

    def moveDiscardPileToDrawPile(self):
        while self.DiscardPile.len() > 0:
            self.DrawPile.drop(self.DiscardPile.draw())
        self.DrawPile.shuffle()

    def moveDrawPileToDiscardPile(self):
        while self.DrawPile.len() > 0:
            self.DiscardPile.drop(self.DrawPile.draw())
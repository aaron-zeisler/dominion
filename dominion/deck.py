
import random

class Pile(object):

    Cards = []

    def __init__(self):
        self.Cards = []

    def draw(self):
        if len(self.Cards) == 0:
            raise Exception("There are no cards in this pile")

        drawnCard = self.pop()
        return drawnCard

    def dropOne(self, card):
        self.push(card)

    def dropMany(self, cards)
        for card in cards:
            self.dropOne(card)

    def shuffle(self):
        if len(self.Cards) == 0:
            return

        random.shuffle(self.Cards)

    def length(self):
        return len(self.Cards)


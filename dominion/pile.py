
import random

class Pile(object):

    Cards = []

    def __init__(self):
        self.Cards = []

    def draw(self):
        if len(self.Cards) == 0:
            raise Exception("There are no cards in this pile")

        drawnCard = self.Cards.pop()
        return drawnCard

    def drop(self, card):
        self.Cards.append(card)

    def shuffle(self):
        if len(self.Cards) == 0:
            return

        random.shuffle(self.Cards)

    def len(self):
        return len(self.Cards)


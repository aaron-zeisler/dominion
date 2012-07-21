
class Hand(object):

    Cards = []

    def __init__(self):
        self.Cards = []

    def draw(self, card):
        self.Cards.append(card)

    def discard(self, card):
        for c in self.Cards:
            if c.Name == card.Name:
                self.Cards.remove(c)
                return c
        return None

    def len(self):
        return len(self.Cards)

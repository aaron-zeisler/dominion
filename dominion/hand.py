
class Hand(object):

    Cards = []

    def __init__(self):
        self.Cards = []
        pass

    def draw(self, card):
        self.cards.append(card)

    def discard(self, cardName):
        for card in self.Cards:
            if card.Name == cardName:
                self.Cards.remove(card)
                return card
        return None

    def discardAll(self):
        oldHand = self.Cards
        self.Cards = []
        return oldHand

    def length(self):
        return len(self.Cards)

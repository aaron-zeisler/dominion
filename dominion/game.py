
from dominion.supply_area import SupplyArea as SupplyAreaClass
from dominion.card import Card
from dominion.pile import Pile
from dominion.cards import cards, decks

class Game(object):

    Players = []
    SupplyArea = SupplyAreaClass()

    def __init__(self):
        self.Players = []
        self.SupplyArea = SupplyAreaClass()

    def addPlayer(self, player):
        self.Players.append(player)


    def initialize(self):
        #TODO:
        # 0) Load cards from the data source
        allCards = cards

        # 1) Add Copper, Silver, and Gold to the SupplyArea
        copperData = allCards['dominion-copper']
        self._addCardsToPile(self.SupplyArea.CopperPile, copperData, 60)
        silverData = allCards['dominion-silver']
        self._addCardsToPile(self.SupplyArea.SilverPile, silverData, 40)
        goldData = allCards['dominion-gold']
        self._addCardsToPile(self.SupplyArea.GoldPile, goldData, 30)

        # 2) Add Estates, Duchies, and Provinces to the SupplyArea
        numberOfVictoryCards = 12
        if len(self.Players) == 2:
            numberOfVictoryCards = 8
        estateData = allCards['dominion-estate']
        duchyData = allCards['dominion-duchy']
        provinceData = allCards['dominion-province']
        self._addCardsToPile(self.SupplyArea.EstatePile, estateData, numberOfVictoryCards)
        self._addCardsToPile(self.SupplyArea.DuchyPile, duchyData, numberOfVictoryCards)
        self._addCardsToPile(self.SupplyArea.ProvincePile, provinceData, numberOfVictoryCards)
        additionalEstates = len(self.Players) * 3
        self._addCardsToPile(self.SupplyArea.EstatePile, estateData, additionalEstates)

        # 3) Add Curses to the SupplyArea
        curseData = allCards['dominion-curse']
        self._addCardsToPile(self.SupplyArea.CursePile, curseData, 30)

        # 4) Add Kingdom Cards to the SupplyArea
        allDecks = decks
        firstGameDeck = allDecks['first-game']
        for cardName in firstGameDeck:
            cardData = allCards[cardName]
            newPile = Pile()
            self._addCardsToPile(newPile, cardData, 10)
            self.SupplyArea.KingdomPiles[cardData['name']] = newPile

        # 5) Deal Copper and Estate cards to each Player's DrawPile
        for player in self.Players:
            for i in range(3):
                estate = self.SupplyArea.EstatePile.draw()
                player.DrawPile.drop(estate)
            for i in range(7):
                copper = self.SupplyArea.CopperPile.draw()
                player.DrawPile.drop(copper)

        # 6) Shuffle each Player's DrawPile
        for player in self.Players:
            player.shuffle()

        # 7) Have each Player draw 5 cards from their DrawPile into the Hand
        for player in self.Players:
            for i in range(5):
                player.draw()

        pass

    def _addCardsToPile(self, pile, cardData, howMany):
        for i in range(howMany):
            pile.drop(Card(
                name=cardData['name'],
                type=cardData['type'],
                cost=cardData.get('cost', 0),
                effects=cardData.get('effects', None),
                imageUrl=cardData['image']))


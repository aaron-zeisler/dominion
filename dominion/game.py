
from dominion.supply_area import SupplyArea as SupplyAreaClass
from dominion.card import Card
from dominion.pile import Pile
from dominion import dominion_data, dominion_rules

class Game(object):

    Players = []
    SupplyArea = SupplyAreaClass()

    def __init__(self):
        self.Players = []
        self.SupplyArea = SupplyAreaClass()

    def addPlayer(self, player):
        self.Players.append(player)

    def setUpGame(self):
        self._setUpTreasureCards()
        self._setUpVictoryCards()
        self._setUpCurseCards()
        self._setUpKingdomCards()

        self._setUpInitialDecks()
        self._drawFirstHands()

    def _setUpTreasureCards(self):
        # 1) Add Copper, Silver, and Gold to the SupplyArea
        copperData = dominion_data.cards['copper']
        self.SupplyArea.CopperPile = self._makePile(copperData, dominion_rules.GAME_SETUP.COPPER_CARDS)
        silverData = dominion_data.cards['silver']
        self.SupplyArea.SilverPile = self._makePile(silverData, dominion_rules.GAME_SETUP.SILVER_CARDS)
        goldData = dominion_data.cards['gold']
        self.SupplyArea.GoldPile = self._makePile(goldData, dominion_rules.GAME_SETUP.GOLD_CARDS)

    def _setUpVictoryCards(self):
        # 2) Add Estates, Duchies, and Provinces to the SupplyArea
        numberOfVictoryCards = dominion_rules.getGameSetupVictoryCardCount(len(self.Players))
        estateData = dominion_data.cards['estate']
        duchyData = dominion_data.cards['duchy']
        provinceData = dominion_data.cards['province']
        self.SupplyArea.EstatePile = self._makePile(estateData, numberOfVictoryCards)
        self.SupplyArea.DuchyPile = self._makePile(duchyData, numberOfVictoryCards)
        self.SupplyArea.ProvincePile = self._makePile(provinceData, numberOfVictoryCards)
        additionalEstateCount = len(self.Players) * dominion_rules.FIRST_DECK.ESTATE_CARDS
        additionalEstates = self._makePile(estateData, additionalEstateCount)
        self.SupplyArea.EstatePile = self._combinePiles([self.SupplyArea.EstatePile, additionalEstates])

    def _setUpCurseCards(self):
        # 3) Add Curses to the SupplyArea
        curseData = dominion_data.cards['curse']
        self.SupplyArea.CursePile = self._makePile(curseData, dominion_rules.GAME_SETUP.CURSE_CARDS)

    def _setUpKingdomCards(self):
        # 4) Add Kingdom Cards to the SupplyArea
        firstGameDeck = dominion_data.decks['first-game']
        for cardName in firstGameDeck:
            cardData = dominion_data.cards[cardName]
            newPile = self._makePile(cardData, dominion_rules.GAME_SETUP.KINGDOM_CARDS)
            self.SupplyArea.KingdomPiles[cardData['name']] = newPile

    def _setUpInitialDecks(self):
        # 5) Deal Copper and Estate cards to each Player's DrawPile
        for player in self.Players:
            for i in range(dominion_rules.FIRST_DECK.ESTATE_CARDS):
                estate = self.SupplyArea.EstatePile.draw()
                player.DrawPile.drop(estate)
            for i in range(dominion_rules.FIRST_DECK.COPPER_CARDS):
                copper = self.SupplyArea.CopperPile.draw()
                player.DrawPile.drop(copper)

        # 6) Shuffle each Player's DrawPile
        for player in self.Players:
            player.shuffle()

    def _drawFirstHands(self):
        # 7) Have each Player draw 5 cards from their DrawPile into the Hand
        for player in self.Players:
            player.drawHand()

    def _makePile(self, cardData, howManyCards):
        pile = Pile()
        for i in range(howManyCards):
            pile.drop(Card(
                name=cardData['name'],
                type=cardData['type'],
                cost=cardData.get('cost', 0),
                effects=cardData.get('effects', None),
                imageUrl=cardData['image']))

        return pile

    def _combinePiles(self, pileArray):
        newPile = Pile()
        for pile in pileArray:
            for card in pile.Cards:
                newPile.drop(card)
        return newPile


    def over(self):
        # The game is over if ...
        # 1) The Province pile is empty, or
        # 2) any 3 piles are empty
        if self.SupplyArea.ProvincePile.len() == 0:
            return True

        emptyPiles = 0
        for cardName, pile in self.SupplyArea.allPiles().iteritems():
            if pile.len() == 0:
                emptyPiles += 1
                if emptyPiles >= 3:
                    return True

        return False

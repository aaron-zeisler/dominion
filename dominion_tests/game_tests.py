
import unittest
from dominion_tests.dominion_test import DominionTest
from dominion import dominion_rules, dominion_data
from dominion.game import Game
from dominion.player import Player
from dominion.pile import Pile


class MyTestCase(DominionTest):
    def test__init__(self):
        game = Game()
        self.assertEqual(game.Players, [])
        self.assertEqual(game.SupplyArea.KingdomPiles, {})

    def test_addPlayer(self):
        game = Game()
        game.addPlayer(Player(name="Test Player"))
        self.assertEqual(len(game.Players), 1)
        self.assertEqual(game.Players[0].Name, "Test Player")

    def test_setUpGame(self):
        self.mocker.StubOutWithMock(Game, '_setUpTreasureCards')
        Game._setUpTreasureCards()
        self.mocker.StubOutWithMock(Game, '_setUpVictoryCards')
        Game._setUpVictoryCards()
        self.mocker.StubOutWithMock(Game, '_setUpCurseCards')
        Game._setUpCurseCards()
        self.mocker.StubOutWithMock(Game, '_setUpKingdomCards')
        Game._setUpKingdomCards()
        self.mocker.StubOutWithMock(Game, '_setUpInitialDecks')
        Game._setUpInitialDecks()
        self.mocker.StubOutWithMock(Game, '_drawFirstHands')
        Game._drawFirstHands()
        self.mocker.ReplayAll()

        game = Game()
        game.setUpGame()
        self.mocker.VerifyAll()

    def test__setUpTreasureCards(self):
        self.mocker.StubOutWithMock(Game, '_makePile')
        Game._makePile(dominion_data.cards['dominion-copper'], dominion_rules.GAME_SETUP.COPPER_CARDS).AndReturn("copper pile")
        Game._makePile(dominion_data.cards['dominion-silver'], dominion_rules.GAME_SETUP.SILVER_CARDS).AndReturn("silver pile")
        Game._makePile(dominion_data.cards['dominion-gold'], dominion_rules.GAME_SETUP.GOLD_CARDS).AndReturn("gold pile")
        self.mocker.ReplayAll()

        game = Game()
        game._setUpTreasureCards()
        self.assertEqual(game.SupplyArea.CopperPile, "copper pile")
        self.assertEqual(game.SupplyArea.SilverPile, "silver pile")
        self.assertEqual(game.SupplyArea.GoldPile, "gold pile")
        self.mocker.VerifyAll()

    def test__setUpVictoryCards(self):
        victoryCards = 10
        self.mocker.StubOutWithMock(dominion_rules, 'getGameSetupVictoryCardCount')
        self.mocker.StubOutWithMock(Game, '_makePile')
        self.mocker.StubOutWithMock(Game, '_combinePiles')
        dominion_rules.getGameSetupVictoryCardCount(0).AndReturn(victoryCards)
        Game._makePile(dominion_data.cards['dominion-estate'], victoryCards).AndReturn("estate pile")
        Game._makePile(dominion_data.cards['dominion-duchy'], victoryCards).AndReturn("duchy pile")
        Game._makePile(dominion_data.cards['dominion-province'], victoryCards).AndReturn("province pile")
        Game._makePile(dominion_data.cards['dominion-estate'], 0).AndReturn("additional estates")
        Game._combinePiles(["estate pile","additional estates"]).AndReturn("updated estate pile")
        self.mocker.ReplayAll()

        game = Game()
        game._setUpVictoryCards()
        self.assertEqual(game.SupplyArea.EstatePile, "updated estate pile")
        self.assertEqual(game.SupplyArea.DuchyPile, "duchy pile")
        self.assertEqual(game.SupplyArea.ProvincePile, "province pile")
        self.mocker.VerifyAll()

    def test__setUpCurseCards(self):
        self.mocker.StubOutWithMock(Game, '_makePile')
        Game._makePile(dominion_data.cards['dominion-curse'], dominion_rules.GAME_SETUP.CURSE_CARDS).AndReturn("curse pile")
        self.mocker.ReplayAll()

        game = Game()
        game._setUpCurseCards()
        self.assertEqual(game.SupplyArea.CursePile, "curse pile")
        self.mocker.VerifyAll()

    def test__setUpKingdomCards(self):
        dominion_data.decks['first-game'] = ['dominion-cellar',
                                             'dominion-market',
                                             'dominion-militia',
                                             'dominion-mine',
                                             'dominion-moat',]
        self.mocker.StubOutWithMock(Game, '_makePile')
        for cardName in dominion_data.decks['first-game']:
            Game._makePile(dominion_data.cards[cardName], dominion_rules.GAME_SETUP.KINGDOM_CARDS).AndReturn("%s pile" % cardName)
        self.mocker.ReplayAll()

        game = Game()
        game._setUpKingdomCards()
        self.assertEqual(len(game.SupplyArea.KingdomPiles), 5)
        self.assertEqual(game.SupplyArea.KingdomPiles['Cellar'], "dominion-cellar pile")
        self.assertEqual(game.SupplyArea.KingdomPiles['Market'], "dominion-market pile")
        self.assertEqual(game.SupplyArea.KingdomPiles['Militia'], "dominion-militia pile")
        self.assertEqual(game.SupplyArea.KingdomPiles['Mine'], "dominion-mine pile")
        self.assertEqual(game.SupplyArea.KingdomPiles['Moat'], "dominion-moat pile")
        self.mocker.VerifyAll()

    def test__setUpInitialDecks(self):
        game = Game()
        game.addPlayer(Player(name="Player 1"))
        game.addPlayer(Player(name="Player 2"))
        game.SupplyArea.EstatePile = game._makePile(dominion_data.cards['dominion-estate'], 20)
        game.SupplyArea.CopperPile = game._makePile(dominion_data.cards['dominion-copper'], 20)

        game._setUpInitialDecks()
        for player in game.Players:
            self.assertEqual(player.DrawPile.len(), 10)
        self.assertEqual(game.SupplyArea.EstatePile.len(), (20 - (dominion_rules.FIRST_DECK.ESTATE_CARDS * 2)))
        self.assertEqual(game.SupplyArea.CopperPile.len(), (20 - (dominion_rules.FIRST_DECK.COPPER_CARDS * 2)))

    def test__drawFirstHands(self):
        game = Game()
        game.addPlayer(Player(name="Player 1"))
        game.addPlayer(Player(name="Player 2"))
        estatePile = game._makePile(dominion_data.cards['dominion-estate'], dominion_rules.FIRST_DECK.ESTATE_CARDS)
        copperPile = game._makePile(dominion_data.cards['dominion-copper'], dominion_rules.FIRST_DECK.COPPER_CARDS)
        for player in game.Players:
            firstDeck = game._combinePiles([estatePile, copperPile])
            player.DrawPile = firstDeck

        game._drawFirstHands()
        for player in game.Players:
            self.assertEqual(player.DrawPile.len(), 5)
            self.assertEqual(player.Hand.len(), 5)

    def test_over__notOver(self):
        game = Game()
        game.addPlayer(Player(name="Player 1"))
        game.addPlayer(Player(name="Player 2"))
        game.setUpGame()
        self.assertFalse(game.over())

    def test_over__emptyProvincePile(self):
        game = Game()
        game.addPlayer(Player(name="Player 1"))
        game.addPlayer(Player(name="Player 2"))
        game.setUpGame()

        game.SupplyArea.ProvincePile = Pile()
        self.assertTrue(game.over())

    def test_over__threeEmptyPiles(self):
        game = Game()
        game.addPlayer(Player(name="Player 1"))
        game.addPlayer(Player(name="Player 2"))
        game.setUpGame()

        game.SupplyArea.DuchyPile = Pile()
        for i in range(2):
            game.SupplyArea.KingdomPiles[i] = Pile()
        self.assertTrue(game.over())

if __name__ == '__main__':
    unittest.main()

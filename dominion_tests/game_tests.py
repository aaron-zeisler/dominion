__author__ = 'zed'

import unittest
from dominion.game import Game
from dominion.player import Player


class MyTestCase(unittest.TestCase):
    def test_mock_game(self):
        game = Game()

        playerOne = Player(name="Player One")
        playerTwo = Player(name="Player Two")
        game.addPlayer(playerOne)
        game.addPlayer(playerTwo)

        game.initialize()

        print "DEBUG: The game looks like this: %s" % game.__dict__
        print "DEBUG: The SupplyArea looks like this:"
        print "Copper (%s)" % game.SupplyArea.CopperPile.len()
        print "Silver (%s)" % game.SupplyArea.SilverPile.len()
        print "Gold (%s)" % game.SupplyArea.GoldPile.len()
        print "Estate (%s)" % game.SupplyArea.EstatePile.len()
        print "Duchy (%s)" % game.SupplyArea.DuchyPile.len()
        print "Province (%s)" % game.SupplyArea.ProvincePile.len()
        print "Curse (%s)" % game.SupplyArea.CursePile.len()
        for pileName, pile in game.SupplyArea.KingdomPiles.iteritems():
            print "%s (%s)" % (pileName, pile.len())
        print "DEBUG: Here are the players' draw piles:"
        for player in game.Players:
            print "%s:" % player.Name
            print "DECK:"
            for card in player.DrawPile.Cards:
                print card.Name
            print "HAND:"
            for card in player.Hand.Cards:
                print card.Name

if __name__ == '__main__':
    unittest.main()

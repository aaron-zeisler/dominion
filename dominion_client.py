
from dominion.game import Game
from dominion.player import Player
from dominion.turn import Turn

class DominionClient():
    def main(self):
        game = Game()

        playerOne = Player(name="Player One")
        playerTwo = Player(name="Player Two")
        game.addPlayer(playerOne)
        game.addPlayer(playerTwo)

        game.setUpGame()

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

        while not game.over():
            for player in game.Players:
                currentTurn = Turn()

                # Count the number of coins
                for card in player.Hand.Cards:
                    currentTurn.Coins += card.Effects.get('coins', 0)

                print "-- %s --" % player.Name
                while currentTurn.ActionsLeft > 0 or currentTurn.BuysLeft > 0:
                    # Choose a card to play
                    cardNumber = None
                    while cardNumber is None:
                        # Display the player's hand and options
                        print "You have %s actions, %s buys, and %s coins" % (currentTurn.ActionsLeft, currentTurn.BuysLeft, currentTurn.Coins)
                        print "Your hand is"
                        for i in range(player.Hand.len()):
                            print "%s: %s" % (i, player.Hand.Cards[i].Name)

                        # Get user input for the card to play
                        try:
                            cardNumber = input("Choose a card to play (enter the number), or 100 to buy, or 99 to end: ")
                        except (IndexError, NameError) as e:
                            print "That isn't an available option.  Try again."
                            cardNumber = None


                    # Player is ending the turn ...
                    if cardNumber == 99:
                        break

                    # Player is buying a card ...
                    elif cardNumber == 100:
                        # Make sure the player has enough buys
                        if currentTurn.BuysLeft == 0:
                            print "You don't have another buy"
                        else:
                            # Get player input for the card to buy
                            buyCardName = None
                            while buyCardName is None:
                                try:
                                    print "The available cards are"
                                    for cardName, pile in game.SupplyArea.allPiles().iteritems():
                                        print "%s (%s coins) (%s left)" % (cardName, pile.Cards[0].Cost, pile.len())
                                    buyCardName = raw_input("Enter the name of the card you wish to buy: ")
                                    buyCard = game.SupplyArea.allPiles()[buyCardName].Cards[0]
                                except (NameError, KeyError) as e:
                                    print "That isn't an option.  Try again"
                                    buyCardName = None

                            buyCardCost = game.SupplyArea.allPiles()[buyCardName].Cards[0].Cost
                            # Make sure the player has enough coins
                            if buyCardCost > currentTurn.Coins:
                                print "You don't have enough coins to buy that card"
                            else:
                                # Buy the card
                                currentTurn.Coins -= buyCardCost
                                currentTurn.BuysLeft -= 1
                                player.DiscardPile.drop(game.SupplyArea.allPiles()[buyCardName].draw())


                    # Player is playing a card from the hand ...
                    elif cardNumber < 100:
                        try:
                            card = player.Hand.Cards[int(cardNumber)]
                            if card.Type.startswith("Action"):
                                # Make sure the player has enough actions
                                if currentTurn.ActionsLeft == 0:
                                    print "You don't have any actions left"
                                else:
                                    currentTurn.ActionsLeft -= 1
                                    currentTurn = self._applyCardEffects(card, currentTurn, player)
                            else:
                                currentTurn = self._applyCardEffects(card, currentTurn, player)

                            player.discard(card)
                        except IndexError, e:
                            print "That isn't an option.  Try again"

                print "Your turn is over"
                print ""
                player.discardHand()
                player.drawHand()

        print "The Game Is Over"

    def _applyCardEffects(self, card, turn, player):
        turn.ActionsLeft += card.Effects.get('actions', 0)
        turn.BuysLeft += card.Effects.get('buys', 0)
        turn.Coins += card.Effects.get('coins', 0)
        for i in range(card.Effects.get('cards', 0)):
            drawnCard = player.draw()
            turn.Coins += drawnCard.Effects.get('coins', 0)
        return turn

if __name__ == '__main__':
    client = DominionClient()
    client.main()
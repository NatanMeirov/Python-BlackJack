# Most of the initializations (Selection and Creation) happens here, in the Background, instead of in the UI. FOR EXAMPLE - Instead of asking to send a reference to a deck instance that created in the UI (when creating a new "ComputerDealer"), the system will create an instance of the deck here, in the background. (this is more safe, and less complicated then in the UI). [This is like an "Encapsulation", or a "Facade" Design Pattern.]
# This is the Builder Design Pattern (from the Creational Group) - to construct complicated objects in the background.
# This will make the UI script look "clean" and easy to understand (Trying to avoid the creation of objects in the UI).

# Import the Game Classes to the Builder script from the (current) BlackJackGameLogic module:

from BlackJackGameLogic import BlackJackGameClasses

class PlayerBuilder():

    @staticmethod
    def build_player(name_of_player, chips_to_start_the_game):
        """
        [summary]
        Builder Design Pattern, building the complicated Player object in the background
        Returning the new Player instance.

        Arguments:
            name_of_player {[Str]} -- [a string of the name of the player]
            chips_to_start_the_game {[int]} -- [number of the chips for the player, in the start of the game]
        """

        new_player = BlackJackGameClasses.Player(name_of_player, BlackJackGameClasses.Hand(), BlackJackGameClasses.Chips(chips_to_start_the_game))
        return new_player

class ComputerDealerBuilder():

    @staticmethod
    def build_dealer():
        """
        [summary]
        Builder Design Pattern, building the complicated ComputerDealer object in the background
        Returning the new ComputerDealer instance.
        """

        new_dealer = BlackJackGameClasses.ComputerDealer(BlackJackGameClasses.Deck(), BlackJackGameClasses.Hand())
        return new_dealer





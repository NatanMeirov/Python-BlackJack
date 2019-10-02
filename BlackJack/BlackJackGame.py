# This is the main script of BlackJack Game (the main Program):
# This is a CONSOLE UI game.

# Import the Game Classes to the main script from the BlackJackGameLogic module:

from BlackJackGameLogic import BlackJackGameClasses
from BlackJackGameLogic import BlackJackGameBuilders

# Main "Static Singleton" game class (with static Game.run() method and global "static" game_state boolean - > No need Game() instance):
class Game():

    game_state = True
    is_player_turn = True # The first move of the game is the player's move

    @staticmethod
    def taking_int_input_from_user(msg_to_user):
        """
        [summary]
        Taking an int input from the user (checks if legal input -> num: int)

        Arguments:
            msg_to_user {[str]} -- [message to print to the user]
        """
        is_correct = False
        while not is_correct:
            try:
                num_from_user = int(input(msg_to_user))

                if num_from_user <= 0: # In case of wrong int value input (like num <= 0)
                    raise ValueError

                is_correct = True # If we are here, then the input is good.

            except:
                print("Please enter a LEGAL number (an integer).")
                is_correct = False

        return num_from_user

    @staticmethod
    def take_bet_from_player(player):
        """
        [summary]
        Taking an input (int) from player. The input is the player's bet (with chips)

        Arguments:
           player {[Player]} -- [a reference to the player object, to check if the input is legal (if the player has enough chips)]
        """
        is_correct = False
        while not is_correct:
            try:
                chips_to_bet = Game.taking_int_input_from_user("Please enter your bet (chips [integer]), considering your current chips balance: ")
                if chips_to_bet > player.chips.total_chips:
                    raise ValueError
                else: # Input is OK and the player has enough chips
                    player.chips.make_bet(chips_to_bet)
                    is_correct = True
            except:
                print(f"You don't have enought chips, your have: ({player.chips.count_total_chips()}). Please enter a legal number of chips.")
                is_correct = False

        return chips_to_bet

    @staticmethod
    def player_hit(player, dealer):
        """
        [summary]
        Hitting (adding) new card to the player's hand from the dealer's deck

        Arguments:
            player {[Player]} -- [a reference to a player object, to add the card to his hand]
            dealer {[ComputerDealer]} -- [a reference to a dealer object, to add the card to the player from his deck]
        """

        player.hand.add_new_card(dealer)
        player.hand.adjust_for_ace()

    @staticmethod
    def dealer_hit(dealer):
        """
        [summary]
        Hitting (adding) new card to the dealer's hand from its deck

        Arguments:
            dealer {[ComputerDealer]} -- [a reference to a dealer object, to add the card to its hand from its deck]
        """

        dealer.hand.add_new_card(dealer)
        dealer.hand.adjust_for_ace()

    @staticmethod
    def player_hit_or_stand(player, dealer):
        """
        [summary]
        Ask the player to choose between Hit or Stand (Hit -> add new card to his hand, Stand -> stand with his cards)
        If the player choose to Hit -> using player_hit() method with the references of the player and the dealer

        Arguments:
            player {[Player]} -- [a reference to a player object, to add the card to his hand - if the player choose to  hit]
            dealer {[ComputerDealer]} -- [a reference to a dealer object, to add the card to the player from his deck if the player choose to  hit]
        """
        print("Please enter your next move: ")
        is_correct = False
        while not is_correct:
            try:
                answer_from_user = input("Do you want to Hit or Stand? Enter 'H'/'h' to Hit, or 'S'/'s' to Stand: ")
                if answer_from_user == "H" or "h" or "S" or "s":
                    if answer_from_user == "H" or "h":
                        print(f"{player} Hits!")
                        player_hit(player, dealer)
                        is_correct = True
                    elif answer_from_user == "S" or "s":
                        print(f"{player} Stands. \nThe Dealer's Turn.")
                        Game.is_player_turn = False
                        is_correct = True
                    else:
                        raise ValueError
            except:
                print("Wrong input, please try again.")
                is_correct = False

    @staticmethod
    def player_bust(player):
        """
        [summary]
        The player busted -> have to decrease his chips that was in the current bet (because of the lose)

        Arguments:
            player {[Player]} -- [a reference to the player (using its name) and to the chips object inside it]
        """
        print(f"{player} BUST!")
        player.chips.losing_bet()

    @staticmethod
    def player_wins(player):
        """
        [summary]
        The player wins -> have to increase his chips that was in the current bet (because of the win)

        Arguments:
            player {[Player]} -- [a reference to the player (using its name) and to the chips object inside it]
        """
        print(f"{player} WINS!")
        player.chips.winning_bet()

    @staticmethod
    def dealer_bust(player, dealer):
        """
        [summary]
        The dealer bust so the player wins -> have to increase the player's chips that was in the current bet (because of the lose of the dealer)

        Arguments:
            player {[Player]} -- [a reference to the player (using its name) and to the chips object inside it]
            dealer {[ComputerDealer]} -- [a reference to the dealer to use its name]
        """
        print(f"{player} WINS! \n{dealer} BUSTED!")
        player.chips.winning_bet()

    @staticmethod
    def dealer_wins(player, dealer):
        """
        [summary]
        The dealer wins so the player loses -> have to decrease the player's chips that was in the current bet (because of the win of the dealer)

        Arguments:
            player {[Player]} -- [a reference to the player (using its name) and to the chips object inside it]
            dealer {[ComputerDealer]} -- [a reference to the dealer to use its name]
        """
        print(f"{dealer} WINS!")
        player.chips.losing_bet()

    @staticmethod
    def push(player, dealer):
        """
        [summary]
        The player and the dealer tie -> push

        Arguments:
            player {[Player]} -- [a reference to the player to use its name]
            dealer {[ComputerDealer]} -- [a reference to the dealer to use its name]
        """
        print(f"{player} and {dealer} tie! PUSH!")

    @staticmethod
    def ask_for_new_round():
        """
        [summary]
        Asking the player to have a new round (with the same state as before [after the change in its chips at the end of the previous round])
        """
        print("Please enter your choice: ")
        is_correct = False
        while not is_correct:
            try:
                answer_from_user = input("Do you want to play another round (with the current chips you already have)? Enter 'Y'/'y' for 'Yes', or 'N'/'n' for 'No': ")
                if answer_from_user == "Y" or "y" or "N" or "n":
                    if answer_from_user == "Y" or "y":
                        print("New round! \nGet ready!")
                        Game.game_state = True
                        is_correct = True
                    elif answer_from_user == "N" or "n":
                        print("Thanks for playing!")
                        Game.game_state = False
                        is_correct = True
                else:
                    raise ValueError
            except:
                print("Wrong input, please try again.")
                is_correct = False

    @staticmethod
    def ask_to_restart_the_whole_game():
        """
        [summary]
        Asking the player to restart the whole game (running Game.run() method again)
        """
        print("Please enter your choice: ")
        is_correct = False
        while not is_correct:
            try:
                answer_from_user = input("Would you like to restart the whole game? Enter 'Y'/'y' for 'Yes', or 'N'/'n' for 'No': ")
                if answer_from_user == "Y" or "y" or "N" or "n":
                    if answer_from_user == "Y" or "y":
                        Game.game_state = True
                        is_correct = True
                        Game.run() # Running the whole game again -> Restart.
                    elif answer_from_user == "N" or "n":
                        Game.game_state = False
                        is_correct = True
                else:
                    raise ValueError
            except:
                print("Wrong input, please try again.")
                is_correct = False

    @staticmethod
    def run():
        """
        [summary]
        The main flow method of the game (Static class method -> No need Game() instance)
        """
        # Pre-game settings:

        print("This is a Console UI BlackJack Game.")
        print("\n")
        print("You are going to play against a Computer - 'The Dealer'.")
        print("What is you name?")
        name_of_player = str(input("Please enter you name: "))
        print(f"Hello {name_of_player}!")
        starting_chips = Game.taking_int_input_from_user("With how many chips do you want to start the game? ")
        print("\n")

        player = BlackJackGameBuilders.PlayerBuilder.build_player(name_of_player, starting_chips)
        dealer = BlackJackGameBuilders.ComputerDealerBuilder.build_dealer()
        dealer.deck.shuffle()

        # Initializing the first hand of the game:

        player.set_new_hand() # Although this line isn't needed, it is more readable to see it here in the game flow.
        player.current_hand.add_new_card(dealer)
        player.current_hand.add_new_card(dealer)
        dealer.set_new_hand()
        dealer.current_hand.add_new_card(dealer)
        dealer.current_hand.add_new_card(dealer)

        # Start of the game loop:
        print(f"Finally.....GAME IS ON! \nGood Luck {player}!")
        while Game.game_state:
            Game.is_player_turn = True
            print("\n" * 3)

            current_player_bet = Game.take_bet_from_player(player)
            print(f"Your bet is: {current_player_bet}.")
            print("\n")

            print(f"{player} has: ")
            print(player.show_hand())
            print("\n")
            print(f"{dealer} has: ")
            print(dealer.show_dealer_one_card())

            while Game.is_player_turn:
                Game.player_hit_or_stand(player, dealer)
                print(f"{player} has: ")
                print(player.show_hand())
                print("\n")
                print(f"{dealer} has: ")
                print(dealer.show_dealer_one_card())

                if player.current_hand.value_of_cards_in_hand > 21:
                    Game.player_bust(player)
                    break

            if player.current_hand.value_of_cards_in_hand <=21:
                while dealer.current_hand.value_of_cards_in_hand < 17: # Soft 17 (BlackJack Rule)
                    Game.dealer_hit(dealer)

                print(f"{player} has: ")
                print(player.show_hand())
                print("\n")
                print(f"{dealer} has: ")
                print(dealer.show_hand())

                if dealer.current_hand.value_of_cards_in_hand > 21:
                    Game.dealer_bust(player, dealer)
                elif dealer.current_hand.value_of_cards_in_hand > player.current_hand.value_of_cards_in_hand:
                    Game.dealer_wins(player, dealer)
                elif dealer.current_hand.value_of_cards_in_hand < player.current_hand.value_of_cards_in_hand:
                    Game.player_wins(player)
                elif dealer.current_hand.value_of_cards_in_hand == player.current_hand.value_of_cards_in_hand: # Could just write - else (but used elif to be clear what is the situation)
                    Game.push(player, dealer)

            print("\n")
            print(f"\n{player}'s {player.chips.count_total_chips}")

            if player.chips.total_chips > 0: # If still have some chips "to spend" in a new round
                Game.ask_for_new_round()
            else:
                Game.game_state = False

        Game.ask_to_restart_the_whole_game()





if __name__ == "__main__":
    Game.run()
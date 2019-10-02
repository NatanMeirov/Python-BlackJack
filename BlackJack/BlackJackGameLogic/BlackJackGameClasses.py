# This is the BlackJack Game Classes script (The Logic of the game).
# This module gives the option to REUSE the whole BlackJack Game Clases functionality, with other BlackJack Game UI.

# Libraries in use in this BlackJack Game Classes script:

import random

# Game class objects:

class GameSettings():
    # Global Game (Settings) variables
    suits = ("Hearts", "Diamonds", "Spades", "Clubs")
    ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
    values = {"Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5, "Six" : 6, "Seven" : 7, "Eight" : 8, "Nine" : 9, "Ten" : 10, "Jack" : 10, "Queen" : 10, "King" : 10, "Ace" : 11} # Ace can actually be - or 1, or 11

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def show_card(self):
        """
        [summary]
        Showing the current card
        """
        return self.__str__() # Using __str__() method of (self) Card class object

class Deck():
    # Initialization of the deck (list of cards):
    def __init__(self):
        self.list_of_cards = []
        for suit in GameSettings.suits:
            for rank in GameSettings.ranks:
                self.list_of_cards.append(Card(suit, rank))

    # String presentation of the current deck state:
    def __str__(self):
        deck_composition = ""
        for card in self.list_of_cards:
            deck_composition +=  "\n" + card.show_card()

        return f"The deck has: {deck_composition}\n"

    def show_deck(self):
        """
        [summary]
        Showing the current deck
        """
        return self.__str__() # Using __str__() method of (self) Deck class object

    def shuffle(self):
        """
        [summary]
        Shuffles the deck.
        """
        random.shuffle(self.list_of_cards)

    def deal(self):
        """
        [summary]
        Return the card in the top of the deck (the first card in the list -> index [0]).
        """
        return self.list_of_cards.pop(0)

class Hand():
    def __init__(self):
        self.cards_in_hand = [] # Starts with an empty list of cards
        self.value_of_cards_in_hand = 0
        self.num_of_aces_in_hand_to_decrease_value_if_needed = 0

    # Showing the cards in the current hand
    def __str__(self):
        cards_to_show = ""
        for card in self.cards_in_hand:
            cards_to_show += "\n" + card.show_card()

        return cards_to_show

    def get_cards(self):
        """
        [summary]
        Returning the cards list
        """
        return self.cards_in_hand

    def add_new_card(self, dealer):
        """
        [summary]
        Adding new card to the hand (append this card object to the list of cards).
        Adding the value to the current hand value (using the global values dictionary).
        If the card's rank is Ace, add +1 to the number of Aces.

        Arguments:
            dealer {[ComputerDealer]} -- [deal a card from the dealer to add to the hand. Using dealer.deck.deal() -> Card(suit, rank)]
        """
        card_to_add = dealer.deck.deal()
        self.cards_in_hand.append(card_to_add)
        self.value_of_cards_in_hand += GameSettings.values[card_to_add.rank]

        if card_to_add.rank == "Ace":
            self.num_of_aces_in_hand_to_decrease_value_if_needed += 1

    def adjust_for_ace(self):
        """
        [summary]
        While the player has more then 21 value in his current hand, and has an Ace(s),
        then the value of each Ace decrease to 1 (instead of 11)
        """
        while self.value_of_cards_in_hand > 21 and self.num_of_aces_in_hand_to_decrease_value_if_needed > 0:
            self.value_of_cards_in_hand -= 10 # Counting the ace as 1 instead of 11 (BlackJack rule)
            self.num_of_aces_in_hand_to_decrease_value_if_needed -= 1

class Chips():

    def __init__(self, total_chips):
        self.total_chips = total_chips
        self.current_bet = 0

    def __str__(self):
        return f"Total chips: {self.total_chips}"

    def count_total_chips(self):
        """
        [summary]
        Showing the current sum of the total chips of the player.
        """
        return self.__str__() # Using __str__() method of (self) Chips class object

    def winning_bet(self):
        """
        [summary]
        Adding the winning bet chips to the total chips sum of the player
        """
        self.total_chips += self.current_bet
        self.current_bet = 0

    def losing_bet(self):
        """
        [summary]
        Decreasing the losing bet chips from the total chips sum of the player
        """
        self.total_chips -= self.current_bet
        self.current_bet = 0

    def make_bet(self, new_bet):
        """
        [summary]
        Player makes new bet

        Arguments:
            new_bet {[int]} -- [Chips that the player bet (decreasing from the total chips and adding to the current bet)]
        """
        self.total_chips -= new_bet
        self.current_bet += new_bet

class Player():

    def __init__(self, name_of_player, hand, chips):
        self.name_of_player = name_of_player
        self.current_hand = hand # Hand class object
        self.chips = chips # Chips class object

    def __str__(self):
        return self.name_of_player

    def set_new_hand(self):
        """
        [summary]
        Setting new empty hand to the player.
        """
        self.current_hand = Hand()


    def show_hand(self):
        """
        [summary]
        Showing the current hand of the player
        """
        return self.current_hand.__str__() # Using __str__() method of Hand class object

class ComputerDealer():

    def __init__(self, deck, hand):
        self.name_of_computer = "The Dealer"
        self.deck = deck
        self.current_hand = hand

    def __str__(self):
        return self.name_of_computer

    def set_new_hand(self):
        """
        [summary]
        Setting new empty hand to the dealer.
        """
        self.current_hand = Hand()


    def show_hand(self):
        """
        [summary]
        Showing the current hand of the dealer
        """
        return self.current_hand.__str__() # Using __str__() method of Hand class object

    def show_dealer_one_card(self):
        """
        [summary]
        Getting the cards list from the current_hand (Hand object), and returning just one of them
        """
        cards_in_hand_to_select_one = self.current_hand.cards_in_hand # Getting the 2 cards to a new list
        return f"\n{cards_in_hand_to_select_one[0].__str__()} \nOne Hidden Card!" # Using the __str__() method of the Card() object in index [0] of the cards list
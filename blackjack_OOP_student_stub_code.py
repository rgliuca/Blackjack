import random

class Card:
    CARD_RANKS = ["A░", "2░","3░","4░","5░","6░","7░","8░","9░","10","J░","Q░","K░"]
    CARD_SUITS = ['♠', '♥', '♣', '♦', '░']
    
    CARD_IMAGE_TOP =        '┌─────────┐\t'
    CARD_IMAGE_MIDDLE =     '│░░░░░░░░░│\t'
    CARD_IMAGE_LEFT =       '│░'
    CARD_IMAGE_RIGHT =          '░░░░░░│\t'
    CARD_IMAGE_SUIT_LEFT =  '│░░░░'
    CARD_IMAGE_SUIT_RIGHT =       '░░░░│\t'
    CARD_IMAGE_BOTTOM =     '└─────────┘\t'

    def __init__(self, value):
        '''
        Can't really do error checking of value here, assume value is within 0 and 51
        The proper way of implementing this is with raising an exception when value 
        is out of range.  You want to save this "value" into a private variable.
        '''
        pass

    def get_suit_image(self):
        '''
        This method returns the suit image of a card, could be one of the following:
        '♠', '♥', '♣', '♦', '░'  You can "compute" the suit image based on the 
        value of the card.  You can use CARD_SUITS for the image.
        '''
        pass

    def get_value(self):
        '''
        This method returns an integer from 0 to 12 indicating card face 
        values: "A", "2", "3", ..., "10", "J", "Q", "K"

        An ace "A" would have a value of 0
        A "2" will have a value of 1
        A queen "Q" will have a value of 11

        You can compute this value from the card value initialized in the 
        __init__ method.
        '''
        pass

    def get_rank_image(self):
        '''
        This method returns the rank image which can be one of the floowing:
        "A░", "2░","3░","4░","5░","6░","7░","8░","9░","10","J░","Q░","K░"
        You can use the card value and the CARD_RANK to compute the image
        '''
        pass

    def print(self, covered=False):
        '''
        Prints the image of this poker card to the screen
        You should use the above CARD_IMAGE_* defines and above helper functions
        to help you print the card image.  
        '''
        pass

    def get_card_image(self, covered=False):
        '''
        Returns the card's image in string, line by line with "\n" to end eeach
        line.  This is similar to Python's __str__() method.
        '''
        pass

    class BJ_Hand:
        # This class implements a hand of BJ cards with following functionality
        #   1. printing the cards out
        #   2. Computes the hand's total value, whether the hand is a bust, etc
        CARD_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        def __init__(self, cards=None):
            pass

        def print(self, msg="", col_size=5, cover_first_card=False):
          # prints the entire hand horizontally, how many cards across? 
            pass
                
        def score(self):
          # returns the value of the entire hand
            pass

        def is_bust(self):
            # returns True/False whether the hand is a bust
            pass

        def get_num_cards(self):
            pass

        def add_card(self, card):
            pass



    class Card_Deck:
        def __init__(self):
            # This function initializes the deck
            # You should create a list of 52 cards in sequence from 0 to 51
            pass

        def shuffle(self):
            # This function shuffles the deck of cards
            # Hint: just shuffle the list of Cards (object)
            pass

        def deal_card(self):
            # This function deals a card from the deck 
            # Just put a card from the list and return it 
            pass

        def get_cards_remaining(self):
            # This function returns the # of cards left in the deck
            pass

    class BJ_Game:
        def __init__(self):
            pass

        def play(self):
            pass


    #########################################
    # simple test on Card and Card_Deck classes 
    #########################################

    # create a new deck of cards
    deck = Card_Deck()

    card1 = deck.deal_card()
    card2 = deck.deal_card()
    card3 = deck.deal_card()

    card1.print_card(show_back=True)
    card1.print_card()
    card2.print_card()
    card3.print_card()

    deck=Card_Deck()

    # deal 52 cards and print out each card (should be in order)
    for i in range(52):
      print("i:",i)
      card=deck.deal_card()
      card.print_card()
      if not i:
        card.print_card(show_back=True)

    # now shuffle the deck of cards
    deck.shuffle()

    # deal 52 cards and print out each card (should be shuffled, random)
    for i in range(52):
      print("i:",i)
      card=deck.deal_card()
      card.print_card()
      if not i:
        card.print_card(show_back=True)

    # test the get_card_image() function
    deck.shuffle()
    card=deck.deal_card()
    card_text=card.get_card_image()
    print("Card Text:")
    print(card_text)


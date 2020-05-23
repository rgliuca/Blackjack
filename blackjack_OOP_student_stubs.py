import random

class Card:
  card_rank=["A░", "2░","3░","4░","5░","6░","7░","8░","9░","10","J░","Q░","K░"]
  card_suit_image=['♠', '♥', '♣', '♦', '░']
  
  line_top=   '┌─────────┐\t'
  line_middle='│░░░░░░░░░│\t'
  line_rank_left= '│░'
  line_rank_right= '░░░░░░│\t'
  line_suit_left=  '│░░░░'
  line_suit_right= '░░░░│\t'
  line_bottom='└─────────┘\t'

  def __init__(self, value):
    # This function initializes the actual card value (a value from 0 to 51)
    pass

  def get_suit_image(self):
    # This function returns one of the card suit image, depends on the card's value
    # You'll have to compute the suit based on the value of the card and 
    # then return one of the element from the card_suit_image list:
    # '♠', '♥', '♣', '♦'
    pass

  def value(self):
    # This function computes the value of the card
    # The value of the card is just an integer value from 1 to 13
    # 1 is for Ace, 2 for 2, ... 12 for Queen and 13 is for King
    pass

  def get_rank_image(self):
    # This function computes the rank based on the card value and returns a
    # string of the following form:
    # "A░", "2░","3░","4░","5░","6░","7░","8░","9░","10","J░","Q░","K░"
    pass

  def print_card(self, print_back=False):
    # This functions prints the poker card (text) image 
    # Example: 
    # ┌─────────┐
    # │░░░░░░░░░│
    # │░J░░░░░░░│
    # │░░░░░░░░░│
    # │░░░░♥░░░░│
    # │░░░░░░░░░│
    # │░░░░░░░░░│
    # │░░░░░░░░░│
    # └─────────┘
    # if the input parameter print_back is True, then you need to print
    # a blank card (the back of a poker card)
    pass

  def get_card_image(self, print_back=False):
    # This function returns a list of string
    # The list contains each line of the poker card's text image
    # BTW, the Card.print_card() function can call this to get the image text list
    # and then print each line out using a loop
    # Example:
    # ['┌─────────┐',
    #  '│░░░░░░░░░│',
    #  '│░J░░░░░░░│',
    #  '│░░░░░░░░░│',
    #  '│░░░░♥░░░░│',
    #  '│░░░░░░░░░│',
    #  '│░░░░░░░░░│',
    #  '│░░░░░░░░░│',
    #  '└─────────┘']
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
    # Just pot a card from the list and return it 
    pass

  def get_cards_remaining(self):
    # This function returns the # of cards left in the deck
    pass



#########################################
# simple test on Card and Card_Deck classes 
#########################################

# create a new deck of cards
deck=Card_Deck()

card1=deck.deal_card()
card2=deck.deal_card()
card3=deck.deal_card()

card1.print_card(print_back=True)
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
    card.print_card(print_back=True)

# now shuffle the deck of cards
deck.shuffle()

# deal 52 cards and print out each card (should be shuffled, random)
for i in range(52):
  print("i:",i)
  card=deck.deal_card()
  card.print_card()
  if not i:
    card.print_card(print_back=True)

# test the get_card_image() function
deck.shuffle()
card=deck.deal_card()
card_text=card.get_card_image()
print("Card Text:")
print(card_text)


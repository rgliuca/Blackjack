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
    pass

  def get_suit_image(self):
    pass

  def value(self):
    pass

  def get_rank_image(self):
    pass

  def print_card(self, print_back=False):
    pass

  def get_card_image(self, print_back=False):
    pass

class Card_Deck:
  def __init__(self):
    pass

  def __create_new_deck__(self):
    pass

  def shuffle(self):
    pass

  def deal_card(self):
    pass

  def get_cards_remaining(self):
    pass



#########################################
# simple test on Card and Card_Deck classes 
#########################################

# create a new deck of cards
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


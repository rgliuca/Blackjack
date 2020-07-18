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
    # Can't really do error checking of value here, assume value is within 0 and 51
    # The proper way of implementing this is with raising an exception when value is out of range
    self.card_value=value

  def get_suit_image(self):
    return self.card_suit_image[self.card_value//13]

  def get_value(self):
    # This is specific to the implementation of BJ
    # To keep it simple for the students, don't use inheritance here, but technically, inheritance is needed 
    # because interpretation of a card value is game specific
    # maybe just let the BJ_hand implement value of a card
    # Thjis method only returns a value from 0-12 indicating "A" - "K"
    return self.card_value%13

  def get_rank_image(self):
    return self.card_rank[self.card_value%13]

  def print_card(self, show_back=False):
    # prints the poker card
    for line in self.get_card_image(show_back):
      print(line)

  def get_card_image(self, show_back=False):
    # returns the card's text, line by line
    # can be used by the caller to print multiple cards line by line
    ct=[]
    ct.append(self.line_top)
    ct.append(self.line_middle)
    ct.append(self.line_middle if show_back else \
      self.line_rank_left+self.get_rank_image()+self.line_rank_right)
    ct.append(self.line_middle if show_back else \
      self.line_suit_left+self.get_suit_image()+self.line_suit_right)
    ct+=[self.line_middle]*3
    ct.append(self.line_bottom)
    return ct

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

class BJ_Game:
  def __init__(self):
    self.poker_cards=Card_Dec()
    self.player=BJ_Hand()
    self.dealer=BJ_Hand()
    self.poker_cards.shuffle()

  def play(self):
    while True:
      if self.poker_cards.get_num_cards_remaining()>=4:
        for i in range(2):
          card=self.poker_cards.deal_card()
          self.player.add_card(card)
          
          self.player.add_card(self.poker_cards.deal_card())
          self.dealer.add_card(self.poker_cards.deal_card())



game=BJ_Game()



#########################################
# simple test on Card and Card_Deck classes 
#########################################

# create a new deck of cards
deck=Card_Deck()

card1=deck.deal_card()
card2=deck.deal_card()
card3=deck.deal_card()

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


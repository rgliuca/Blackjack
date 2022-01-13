class BJ_Game:
  def __init__(self):
    # create the card deck and shuffle it
    self.deck = Card_Deck()
    self.cards.shuffle()

  #Total states: 5

  # State 0: Initial state
  #   Deal cards to the player and the dealer
  #   Display the cards of the player and the dealer
  #   Check if player has Blackjack (A and 10 cards) then goto state 3
  #     if the player has blackjack, then state = 3
  #     else: state = 1


  # State 1: Player plays Blackjack
  # Stay in this state until 3 conditions:
  #    i. the player stays (decides not to take another card)
  #         state = 2
  #    ii. the player busts (went over 21)
  #         state = 3
  #    iii. the card deck is empty when the player hits
  #         state = 4
  #    iv. check for 5 card Charlie
  #    *** I'll let you figure out what states to transition to ***
  #       True: state = 3


  # State 2: Dealer plays Blackjack
  # Stay in this state until the following conditions:
  #    i. dealer keeps hitting until reaching score of 17
  #       if the dealer reaches above 17, but didn't go bust: state = 3
  #    ii. dealer goes bust
  #       state = 3
  #    iii. the card deck is empty when the dealer hits
  #       state = 4


  # State 3: Check winner
  #    i. Computes the scores of each player and dealer
  #    ii. Prints who won the game
  #    iii. Ask if the player wants to play again
  #    iv. If the player wants to play then state = 0
  #          else goto state 4

  # State 4: ending game clean up
  #    If the card deck was empty when the player or dealer hits, then
  #       print "Card deck is empty, Game Over!"
  #       otherwise just print "Game Over!"
  #    exit the program: break from the while True loop!


  def play(self):
    state = 0
    while True:
      if state == 0:
        if self.deck.get_cards_remaining() >= 4:
          self.player = BJ_Hand()
          self.dealer = BJ_Hand()
          for i in range(2):
            self.player.add_card(self.deck.deal_card())
            self.dealer.add_card(self.deck.deal_card())
          print("Player's Hand: ")
          self.player.print()
          print("Dealer's Hand: ")
          self.dealer.print(cover_first_card=True)
          state = 1
          if self.player.score() == 21:
            # player has Blackjack!
            state = 3
        else:
          print("Not enough cards, only", self.deck.get_cards_remaining(), "card(s) left in the deck.")
          state = 4
      elif state == 1:
        # player plays blackjack
        pass

        ans=input("Do you want to hit or stay")
        if ans=='h':
          # check if the deck has at least one more card
          # deal the card to the player
          # check if bust
          # check if 5 card charlie
          #....
          pass
        elif ans=='s':
          state=2
          


        pass
      
      elif state == 2:
        # Dealer plays
        pass

      elif state == 3:
        # check winner
        # display score and check bust or not
        # prompt for continue game or quit
        pass

      elif state == 4:
        # End of the game
        print("Game Over!!!")    
        break


game = BJ_Game()
game.play()

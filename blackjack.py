# Mini-project #6 - Blackjack

import simpleguitk as simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
new_game = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print("Invalid card: ", suit, rank)

    def __str__(self):

        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                          CARD_SIZE)


# define hand class
class Hand:
    def __init__(self):
        self._hand = [] # create Hand object
        self._string = ""

    def __str__(self):
        """
        return a string representation of a hand
        """

        self._string = "Hand contains: "
        for card in self._hand:
            self._string += card.__str__() + ", "
        return self._string[:-2]
    def get_cards(self):
        """
        get the Hand's cards
        """
        return self._hand
    def add_card(self, card):
        """
        add a card object to a hand
        """
        self._hand.append(card)
    def clear(self):
        """
        clear all the Hand
        """
        self._hand = []
        return self._hand

    def get_value(self):
        """
        count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        """
        value = 0
        ranks =[]
        for card in self._hand:  # compute the value of the hand, see Blackjack video
            rank = card.get_rank()
            ranks.append(rank)
            value += VALUES[rank]
            if "A" in ranks and value < 11:
                value += 10
        return value

    def draw(self, canvas, pos):
        """
        draw a hand on the canvas, use the draw method for cards
        """
        for idx in range(len(self._hand)):
            card = self._hand[idx]
            card.draw(canvas, (pos[0] + idx * CARD_SIZE[0], pos[1]))
# define deck class
class Deck:
    def __init__(self):
        """
        create a Deck object
        """
        self._deck = []
        self._string = ""
        for rank in RANKS:
            for suit in SUITS:
                self._deck.append(Card(suit, rank))

    def shuffle(self):
        """
        shuffle the deck
        """
        random.shuffle(self._deck)
        return self._deck

    def deal_card(self):
        """
        deal a card object from the deck
        """
        if len(self._deck) > 0:
            return random.choice(self._deck)

    def __str__(self):
        """
        return a string representing the deck
        """
        self._string += " Deck contains: "
        for card in self._deck:
            self._string += card.__str__() + ","
        return self._string[:-2]
    def is_empty(self):
        """
        check if the Deck is empty
        """
        if self._deck == []:
            return  True
        return False


player_hand = Hand()
dealer_hand = Hand()
deck = Deck()
# define event handlers for buttons
def deal():
    """
     The event handler deal for this button should shuffle the deck (stored as a global variable),
     create new player and dealer hands (stored as global variables), and add two cards to each hand.
    """
    global outcome, in_play, player_hand, dealer_hand, deck, new_game, score
    if deck.is_empty():
        deck = Deck()
    deck.shuffle()
    if new_game:
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        new_game = False
    elif not new_game and in_play:
        start()
        score -= 1
    # else:
    #     if player_hand.get_value() <= 21:
    #         player_hand.add_card(deck.deal_card())
    #         dealer_hand.add_card(deck.deal_card())
    #         if player_hand.get_value() > 21:
    #             outcome = "You have busted."
    #             score -= 1
    #             in_play = False
    #         elif dealer_hand.get_value() > 21:
    #             outcome = "The Dealer has busted. You won."
    #             score += 1
    #             in_play = False
    #         else:
    #             outcome = "This is a tie."
    #             in_play = False
    #             score += 0

def hit():
    """
    If the value of the hand is less than or equal to 21, clicking this button adds an extra card
    to player's hand. If the value exceeds 21 after being hit, print "You have busted".
    """
    global outcome, in_play, player_hand, dealer_hand, score, deck
    deck.shuffle()
    # if the hand is in play, hit the player
    if in_play and player_hand.get_value() <= 21:
        card = deck.deal_card()
        player_hand.add_card(card)
        # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            outcome = "You have busted."
            score += -1
            in_play = False


def stand():
    """
    If the player has busted, remind the player that they have busted. Otherwise, repeatedly hit the dealer until
    his hand has value 17 or more (using a while loop). If the dealer busts, let the player know. Otherwise,
    compare the value of the player's and dealer's hands. If the value of the player's hand is less than or equal to
    the dealer's hand, the dealer wins. Otherwise the player has won.
    """
    global outcome, in_play, player_hand, dealer_hand, score, deck
    deck.shuffle()
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if not in_play and player_hand.get_value() > 21:
        outcome = "You have busted."
    elif not in_play and player_hand.get_value() <= 21:
        outcome = "New game? Click Start."
    else:
        # assign a message to outcome, update in_play and score
        while dealer_hand.get_value() <= 17:
            dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value() > 21:
            outcome = "The Dealer has busted. You won."
            in_play = False
            score += 1
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                outcome = "You won."
                in_play = False
                score += 1
            elif player_hand.get_value() < dealer_hand.get_value():
                outcome = "The Dealer won. You lost"
                in_play = False
                score -= 1
            else:
                outcome = "This is a tie"
                in_play = False


# draw handler
def start():
    global in_play, outcome, score, player_hand, dealer_hand, new_game
    outcome = ""
    score = 0
    player_hand.clear()
    dealer_hand.clear()
    new_game = True
    deal()
    in_play = True

def draw(canvas):
    # test to make sure that card.draw works, replace with your code below

    player_pos = [50, 300]
    player_hand.draw(canvas, player_pos)
    dealer_pos = [50, 130]
    dealer_list = dealer_hand.get_cards()
    card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
    for idx in range(len(dealer_list)):
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [dealer_pos[0] + CARD_BACK_CENTER[0] + idx * CARD_SIZE[0], dealer_pos[1] + CARD_BACK_CENTER[1]] , CARD_SIZE)
    if not in_play:
        dealer_hand.draw(canvas, dealer_pos)
        canvas.draw_text("New Deal? Click Start.", (100, 270), 20,  "White")
    canvas.draw_text("Player's Hand", (50, 290), 15, "Black")
    canvas.draw_text("Dealer's Hand", (50, 120), 15, "Black")
    canvas.draw_text("Score: %s " % score, (400, 50), 15, "Black")
    canvas.draw_text("BlackJack", (70, 70), 35, "Red")
    canvas.draw_text("%s" % outcome, (100, 450), 20, "White")
    if in_play and player_hand.get_value() <= 21:
        canvas.draw_text("Hit or Stand?", (200, 260), 20, "White")



# initialization frame
frame = simplegui.create_frame("Blackjack", 500, 500)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.add_button("Start", start, 200)
frame.set_draw_handler(draw)
start()
# get things rolling
print("player_hand = ", player_hand)
print("dealer_hand = ", dealer_hand)
frame.start()

# remember to review the gradic rubric

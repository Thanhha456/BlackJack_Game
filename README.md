This project is  for assessment in "An Introduction to Interactive Programming in Python (Part 2)" at Rice university.  
https://www.coursera.org/learn/interactive-python-2  

#**MiniProject: BalckJack**#  

Blackjack is a simple, popular card game that is played in many casinos. Cards in Blackjack have the following values: an ace may be valued as either 1 or 11 (player's choice), face cards (kings, queens and jacks) are valued at 10 and the value of the remaining cards corresponds to their number. During a round of Blackjack, the players plays against a dealer with the goal of building a hand (a collection of cards) whose cards have a total value that is higher than the value of the dealer's hand, but not over 21.  (A round of Blackjack is also sometimes r
eferred to as a hand.)  
The game logic for our simplified version of Blackjack is as follows. The player and the dealer are each dealt two cards initially with one of the dealer's cards being dealt faced down (his hole card). The player may then ask for the dealer to repeatedly "hit" his hand by dealing
him another card. If, at any point, the value of the player's hand exceeds 21, the player is "busted" and loses immediately. At any point prior to busting, the player may "stand" and the dealer will then hit his hand until the value of his hand is 17 or more. (For the dealer, ace
s count as 11 unless it causes the dealer's hand to bust). If the dealer busts, the player wins. Otherwise, the player and dealer then compare the values of their hands and the hand with the higher value wins.   

- 1 pt - The program displays the title "Blackjack" on the canvas.
- 1 pt - The program displays 3 buttons ("Deal", "Hit" and "Stand") in the control area.
- 2 pts - The program graphically displays the player's hand using card images. (1 pt if text is displayed in the console instead)
- 2 pts - The program graphically displays the dealer's hand using card images. Displaying both of the dealer's cards face up is allowable when evaluating this bullet. (1 pt if text displayed in the console instead)
- 1 pt - The dealer's hole card is hidden until the current round is over. After the round is over, it is displayed.  
- 2 pts - Pressing the "Deal" button deals out two cards each to the player and dealer. (1 pt per player)
- 1 pt - Pressing the "Deal" button in the middle of the round causes the player to lose the current round.
- 1 pt - Pressing the "Hit" button deals another card to the player.
- 1 pt - Pressing the "Stand" button deals cards to the dealer as necessary.  
- 1 pt - The program correctly recognizes the player busting.
- 1 pt - The program correctly recognizes the dealer busting.
- 1 pt - The program correctly computes hand values and declares a winner. Evaluate based on messages.
- 2 pts - The program accurately prompts the player for an action with messages similar to "Hit or stand?" and "New deal?". (1 pt per message)
- 1 pt - The program implements a scoring system that correctly reflects wins and losses.






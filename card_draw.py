# Corrected Python program to draw five random cards from a shuffled deck.

# importing modules
import itertools
import random

# make a deck of cards
deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))

# shuffle the cards
random.shuffle(deck)

# map card values to their names
card_names = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}

# draw five cards
print("You got:")
for i in range(5):
    value = card_names.get(deck[i][0], deck[i][0])  # Convert value to name if applicable
    print(value, "of", deck[i][1])
"""
Re-order the cards to their original positions (unshuffle them
knowing its riffle shuffling mechanism):

The deck always contains an even nr of cards, so one starts shuffling the deck
into 2 equally sized halves. The magician holds the top half in his left hand
and bottom half in his right hand. During the riffle shuffle, he releases the
bottommost card in each hand, starting with the left, and alternates hands.
As the cards are released, they form a shuffled deck, with the last released card
sitting on top.
You are given the initial order of card indices in the deck, and you must find
the order of the cards after the magician performs the shuffle.

The input is the number of cards N, and the space separated permutation of the
numbers from 1 to N, where every number represents one card in the deck, and
their order is from top to bottom.


# EXAMPLE #1
Input:
6
1 2 3 4 5 6
Output:
4 1 5 2 6 3

# EXAMPLE #2
Input:
4
4 1 3 2
Output:
3 4 2 1
"""

from collections import deque

def unshuffle():
  print "Unshuffling"
  N = int(raw_input())
  shuffled = str(raw_input().strip())
  shuffled = list(shuffled.split())
  unshuffled = []
  mid_index = N/2
  left = deque(shuffled[:mid_index])
  right = deque(shuffled[mid_index:])
  print "unshuffling for N and cards: ",N, " ", shuffled
  index = 0
  while len(right)>0:
    print right[0], " ",
    print left[0], " ",
    right.popleft()
    left.popleft()

unshuffle()

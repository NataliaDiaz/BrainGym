"""
Coin Game
On the table in a single row of N coins, indexed from left to right by numbers
1 to N, every coin has a positive integer value. Filip and Peter are playing a
game where they take turns, with Filip going first. In each turn the current
player picks either the leftmost coin (lowest index) or the rightmost coin
(highest index) and takes it. Both of the players are trying to get the highest
total value (the sum of all the coins they collect). If they both play optimally,
what would be the total value of Filip's coins, and the total value of Peter's
coins when there are no more coins to collect?
(Print first the value of Filip's followed by Peter's score)

# Example #1
Input:
1
10
Output:
10 0

# Example #2
Input:
4
1 2 9 4
Output:
10 6

# Example #3
Input:
9
87 39 23 10 92 19 24 55 91
Output:
199 241
"""

from collections import deque

def get_scores_coin_game(): # N_cards, coins_in_table
  N  = int(raw_input())
  numbers = str(raw_input()).strip().split()
  numbers = map(int, numbers)  #print N, numbers

  numbers = deque(numbers)
  Filip_score = 0
  Peter_score = 0

  if len(numbers) == 0:
    print "0 0"
  elif len(numbers) ==1:
    print numbers[0]," 0"
  else: # more than 1 card
    players_turn = 1 # Filip
    while len(numbers)>0:
      if numbers[0]>= numbers[-1]:
        points = numbers.popleft()
      else:
        points = numbers.pop()
      if players_turn == 1:
        Filip_score += points
        players_turn = 0  # change turn
      else:
        Peter_score += points
        players_turn = 1  # change turn
    print Filip_score," ",Peter_score

get_scores_coin_game()

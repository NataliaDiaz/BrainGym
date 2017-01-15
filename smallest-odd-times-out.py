"""
Return the smallest integer that appears an odd amount of times in a sequence of integers

Example #1
Input:
11
1 1 2 2 3 4 5 6 6 5 4
Output:
3

Example #2
Input:
5
20 10 10 30 10
Output:
10

Numbers are in between 0 and 2^60.
"""

def print_lower_odd_amount_of_appearances():
  N = int(raw_input())
  numbers = str(raw_input()).strip().split()

  sortedn = sorted(numbers)
  print N, sortedn
  n2count = {}
  i =1
  current = sortedn[0]
  while i<N:
    count = 1
    while sortedn[i] == current:
      count +=1
      i +=1
    if count%2 != 0:
      print current
      return current
    current = sortedn[i]
    i +=1



print_lower_odd_amount_of_appearances()

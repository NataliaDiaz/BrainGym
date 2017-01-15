
"""
How many different ways are there of covering a Nx3 grid having available infinite
tiles of size 2x1 and 1x2 in a way that each tile in the grid is covered only
once, and each part of the tile is covering one grid space.
Return the result, as it will be a large number, modulo (10**9)+7.

Example:
Input: 10
Output: 571
"""

def get_n_different_ways_arranging_2x1_1x2_tiles_in_Nx3_grid(N):

  #N = int(raw_input())
  modulo = (10**9)+7
  """
  N ways in a:
  0x3 grid: 0
  1x3 grid: 0
  2x3 grid: 3
  3x3 grid:	0
  4x3 grid: 9
  5x3 grid: 0
  6x3 grid: ...
  """
  if N%3 ==0 or N==0 or N ==1:
    possible_ways = 0
  else:
    if N%2 == 0:
    	possible_ways = 3**(N)
    else:
      	possible_ways = 0 #3**(N-1)
  result = possible_ways % modulo # print "Possible ways and modulo: ", possible_ways, result
  print result
  rturn result


get_n_different_ways_arranging_2x1_1x2_tiles_in_Nx3_grid(0)
get_n_different_ways_arranging_2x1_1x2_tiles_in_Nx3_grid(1)
get_n_different_ways_arranging_2x1_1x2_tiles_in_Nx3_grid(6)
get_n_different_ways_arranging_2x1_1x2_tiles_in_Nx3_grid(10)

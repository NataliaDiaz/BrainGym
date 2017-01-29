#!/bin/python
import sys
import numpy as np

"""
Print the number of squares that the queen can attack from position i,j in the board.
https://www.hackerrank.com/contests/world-codesprint-9/challenges/queens-attack-2

Sample Input 1
4 0
4 4
Sample Output 1
9
Explanation: The queen is standing at position  on a  chessboard with no obstacles
"""

"""
Sample Input 2:
5 3
4 3
5 5
4 2
2 3

Sample Output 2:
10
Explanation: The queen is standing at position  4,3 on a  chessboard with 3 obstacles
"""
def print_nice(m):
    for row in range(len(m)):
        for col in range(len(m[0])):
            print m[row][col],
        print " "
    print '\n'


def attackable_positions(b, i, j, direction):
    """
    Returns the amount of free positions in direction direction from board position i,j in board b
    """
    pos = 0
    n = len(b) #b.shape[0]
    if direction == 'SE':
        while i< n and j<n and b[i][j] ==0:
            i +=1
            j +=1
            pos +=1
    elif direction == 'S':
        while i< n and b[i][j] ==0:
            i += 1
            pos +=1
    elif direction == 'SW':
        while j>=0 and i<n and b[i][j] ==0:
            j -= 1
            i += 1
            pos +=1
    elif direction == 'E':
        while j<n and b[i][j] ==0:
            j += 1
            pos +=1
    elif direction == 'W':
        while j>=0 and b[i][j] ==0:
            j -= 1
            pos +=1
    elif direction == 'NE':
        while i>=0 and j<n and b[i][j] ==0:
            j += 1
            i -=1
            pos +=1
    elif direction == 'NW':
        while i>=0 and j>=0 and b[i][j] ==0:
            j -= 1
            i -=1
            pos +=1
    elif direction == 'N':
        while i>=0 and b[i][j] ==0:
            i -=1
            pos +=1
    else:
        print "Unsupported direction"

    pos -= 1 # because we have counted the position of the queen
    if pos <0:
        pos = 0
    print"Direction ", direction, ":", pos
    return pos

def attackable():
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    if n==0 or n==1:
        print 0
    else:
        rQueen,cQueen = raw_input().strip().split(' ')
        rQueen,cQueen = [int(rQueen)-1,int(cQueen)-1] # input positions are not indexed starting on zero
        attackable = 0
        board = [[0 for i in range(n)] for j in range(n)] #np.zeros((n, n), dtype=np.int)
        for a0 in xrange(k):
            rObstacle,cObstacle = raw_input().strip().split(' ')
            rObstacle,cObstacle = [int(rObstacle)-1,int(cObstacle)-1]
            board[rObstacle][cObstacle] = 1
        # Queen position:     board[rQueen][cQueen]
        print "Board:\n", print_nice(board)
        attackable = attackable_positions(board, rQueen, cQueen, 'N') + attackable_positions(board, rQueen, cQueen, 'S') + attackable_positions(board, rQueen, cQueen, 'E') + attackable_positions(board, rQueen, cQueen, 'W') + attackable_positions(board, rQueen, cQueen, 'NW') + attackable_positions(board, rQueen, cQueen, 'NE') +  attackable_positions(board, rQueen, cQueen, 'SW') + attackable_positions(board, rQueen, cQueen, 'SE')
        print attackable


attackable()

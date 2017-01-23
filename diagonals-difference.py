"""
Given a square matrix of size , calculate the absolute difference between the sums of its diagonals.
Input Format
The first line contains a single integer, . The next  lines denote the matrix's rows, with each line
containing space-separated integers describing the columns.

Output Format
Print the absolute difference between the two sums of the matrix's diagonals as a single integer.

Sample Input
3
11 2 4
4 5 6
10 8 -12

Sample Output
15
"""


def diagonals_difference(n, m):
    d1 = 0
    d2 = 0
    i = 0
    while i<n:
        d1 += m[i][i]
        d2 += m[i][n-1-i]
        i +=1
    result = abs(d1 - d2)
    print result
    return result


diagonals_difference(3,[[11, 2, 4],[4, 5, 6],[10, 8, -12]] )

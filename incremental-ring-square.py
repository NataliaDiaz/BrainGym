import numpy as np

"""
Given N >=1, print a square in which its integer values are represented as rings of integers in expanding increasing order.
E.g.:
N = 2:
222
212
222

N = 3:
33333
32223
32123
32223
33333
"""

def print_nice(m):
    for row in range(len(m)):
        for col in range(len(m[0])):
            print m[row][col],
        print " "
    print '\n'

def paste_matrix_into_larger_in_ij(m, larger_m, i, j):
    larger_m[i:i+m.shape[0], j:j+m.shape[1]] = m
    return larger_m

def incremental_ring_square(n):
    if n==1:
        return [1]
    else:
        # create matrix first filled with zeros
        dim = (n*2)-1
        m = np.zeros(shape=(dim, dim)).astype('int')   #m = []     m.append([1]*dim) for i in range(dim)

        # Fill outermost ring: equals to filling first and last rows, and left and right columns:
        for i in range(dim):
            m[0][i]= n
            m[dim-1][i] = n
            m[i][0]= n
            m[i][dim-1] = n
        # center
        m[dim/2][dim/2]= 1

        # compute smaller rings one at a time
        nested_ring = n-1
        upperLeftCornerStart = 1 # upper left corner coordinates where we start pasting our inner rings
        while nested_ring >=2:
            m = paste_matrix_into_larger_in_ij(incremental_ring_square(nested_ring), m, upperLeftCornerStart, upperLeftCornerStart)
            nested_ring -=1
            upperLeftCornerStart +=1
        return m

print_nice(incremental_ring_square(2))
print_nice(incremental_ring_square(3))
print_nice(incremental_ring_square(4))
print_nice(incremental_ring_square(5))

''' Pascal's Triangle
Difficulty: Easy
Given numRows, generate the first numRows of Pascal's triangle. For example, given numRows = 5, Return
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows ==0:
            return []
        elif numRows ==1:
            return [[1]]
        elif numRows ==2:
            return [[1], [1,1]]
        else:
            triangle = []
            triangle.append([1])
            triangle.append([1,1])
            row = 2
            print "Triangle initialization: ",triangle
            
            while row < numRows:
                newRow = [1]
                for i in xrange(row-1):  # optimize and use insert(pos, elem)
                    upLeft = triangle[row-1][i]
                    upRight = triangle[row-1][i+1]
                    newRow.append(upLeft + upRight)
                newRow.append(1)
                print "New row>", newRow
                triangle.append(newRow)
                row = row+1
            print "Triangle: ", triangle
            return triangle
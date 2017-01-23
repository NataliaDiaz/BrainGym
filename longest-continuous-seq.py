"""
Write a function which takes a list of numbers and returns the length of the
longest continuous stretch of a single number. For example, on the input
[1,7,7,3], the correct return is 2, because there are two 7's in a row.
E.g.
[1,1,1] 3
[1,1,2,2,2] 3
[1,1,2,2,2,2] 4
"""
def longest_continuous_seq(array):
    if len(array)== 0:
        return 0
    else:
        current = array[0]
        index = 1
        solution = 1
        repeats = 1
        while index < (len(array)):
            if current == array[index]:
                repeats += 1
                if repeats> solution:
                    solution = repeats
            else:
                repeats = 1
            current = array[index]
            index +=1
        return solution

longest_continuous_seq([1,1,1])
longest_continuous_seq([1,1,2,2,2])
longest_continuous_seq([1,1,2,2,2,2])

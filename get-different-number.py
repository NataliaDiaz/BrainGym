'''
Getting a Different Number 
Given an array arr of n unique non-negative integers, how can you most
efficiently find a non-negative integer that is not in the array?
Your solution should return such an integer or null if arr contains all possible integers.
Analyze the runtime and space complexity of your solution.
'''


# My valid answer:
def getDifferentNumber(arr):
	mySet = set(arr)
	for i in range(0, MAX_INTEGER):
		if i not in mySet:
			return i
	return null

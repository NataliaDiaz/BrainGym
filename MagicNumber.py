'''MagicNumber
Elegant solution without converting to string and stopping, returning False if n< 10 and n!= 1:  class Solution(object):

My similar solution:'''


class Solution(object):

	#memoizingSubProblems = {}


	def isHappy(self, n):

		"""

		:type n: int

		:rtype: bool

		"""

		print "Executing isHappy(",n,")"

		if n<1:

			return False

		elif n == 1:

			return True

		else:

			sum =0

			while ((n / 10) >= 1): # for each digit (get each digit by getting % 10)

				sum += (n % 10)**2

				n /= 10   # much more inefficient: for digit in list(str(n)):

			sum += (n % 10)**2


			if sum ==1:

				return True

			elif (sum < 10):

				return False

			else:
				return self.isHappy(sum)
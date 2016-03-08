# Write a program to check whether a given number is an ugly number. Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7. Note that 1 is typically treated as an ugly number.

import math


class Solution(object):


	def __init__(self):

		self.uglyFactors = [5,3,2]


	def isPrime(self, n):

		if n<0:

			return False

		if n==1 or n==2:

			return True

		if n % 2 == 0 and n > 2: 

			return False

		for i in range(3, int(n**0.5) + 1):

			if n % i == 0:

				return False

		return True



	def isUgly(self, num):

		"""

		:type num: int

		:rtype: bool

		"""

		if num<=0:

			return False

		if num==1 or num==2:

			return True

		if self.isPrime(num) and not num in self.uglyFactors:

			return False

		for i in range(2, int(num**0.5) + 1): #int(math.sqrt(num))+1, 2):

			if num%i ==0: 

				if not i in self.uglyFactors and self.isPrime(i):

					return False

			factor = num/i

			if not factor in self.uglyFactors and self.isPrime(factor):

			return False

			return True
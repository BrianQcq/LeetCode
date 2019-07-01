"""
Given two integers dividend and divisor, 
divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Input: dividend = 10, divisor = 3
Output: 3

Input: dividend = 7, divisor = -3
Output: -2
"""

class Solution(object):
	def divide(self, dividend, divisor):
		positive = (dividend > 0) is (divisor > 0)
		dividend, divisor = abs(dividend), abs(divisor)
		res = 0

		while dividend >= divisor:
			temp, i = divisor, 1
			while dividend >= temp:
				dividend -= temp
				res += i
				i <<= 1
				temp <<= 1
		if not positive:
			res = -res
		return min(max(res, -2**31), 2**31-1)

A=Solution()
res=A.divide(100, 3)
print(res)

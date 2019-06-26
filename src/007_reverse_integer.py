"""
Given a 32-bit signed integer, reverse digits of an integer.

Input: 123
Output: 321

Input: 120
Output: 21
"""

class Solution(object):
	def reverse(self, x):

		#Edge case consideration
		if x > 2**31 or x < -(2**31):
			return 0
		sign = 1
		if x < 0:
			sign = -1
		if x % 10 == 0:
			x = x // 10

		temp = str(sign * x)[::-1]
		res = sign * int(temp)
		if res > 2**31 or res < -(2**31):
			return 0
		return res


A=Solution()
res=A.reverse(-99010)
print(res)
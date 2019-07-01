"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Input: 2.00000, 10
Output: 1024.00000

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""

class Solution(object):

	# recursive
	def myPow(self, x, n):
		if not n:
			return 1
		if n < 0:
			return 1 / self.myPow(x, -n)
		if n % 2:
			return x * self.myPow(x, n-1)
		return self.myPow(x*x, n//2)

	# iterative
	def myPow_2(self, x, n):
		if n < 0:
			x = 1 / x
			n = -n
		res = 1
		while n:
			if n & 1:
				res *= x
			x *= x
			n >>= 1
		return res

A=Solution()
res=A.myPow(2.0, 10)
res2=A.myPow_2(1.1, -10)
print(res)
print(res2)
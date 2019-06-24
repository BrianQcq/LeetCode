"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Input: 121
Output: true

Input: -121
Output: false
"""

class Solution(object):
	#Converting to string, extra space required.
	def isPalindrome(self, x):
		temp = str(x)
		return temp == temp[::-1]

	#If O(1) extra space.
	def isPalindrome_2(self, x):
		if x < 0:
			return False
		p, res = x, 0
		while p:
			res = res * 10 + p % 10
			p = p // 10
		return res == x

A=Solution()
res=A.isPalindrome_2(1221)
print(res)
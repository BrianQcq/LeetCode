"""
Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: "cbbd"
Output: "bb"
"""

class Solution(object):
	def longestPalindrome(self, s):
		res = ""
		for i in range(len(s)):
			temp = self.helper(s,i,i)
			if len(temp) > len(res):
				res = temp

			temp = self.helper(s,i,i+1)
			if len(temp) > len(res):
				res = temp
		return res

	def helper(self, s, l, r):
		while l >= 0 and r < len(s) and s[l] == s[r]:
			l -= 1; r += 1
		return s[l+1:r]

# DP solution

class Solution2(object):
	def longestPalindrome(self, s):
		if len(s) == 0:
			return 0
		maxLen = 1
		start = 0
		for i in range(len(s)):
			pass

A=Solution()
res=A.helper("babac", 1, 1)
print(res)
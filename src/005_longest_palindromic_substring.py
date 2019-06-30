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
		pass

	def helper(self, s, l, r):
		while l >= 0 and r < len(s) and s[l] == s[r]:
			l -= 1; r += 1
		return s[l+1:r]



A=Solution()
res=A.helper("abaac", 3, 3)
print(res)
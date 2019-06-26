"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Input: "A man, a plan, a canal: Panama"
Output: true
"""

class Solution(object):

	# naive solution
	def isPalindrome(self, s):
		temp = ''
		for item in s:
			if item.isalnum():
				temp += item.lower()
		return temp == temp[::-1]

	# in place two-pointer solution
	def isPalindrome_2(self, s):
		l, r = 0, len(s) - 1
		while l < r:
			while l < r and not s[l].isalnum():
				l += 1
			while l < r and not s[r].isalnum():
				r -= 1
			if s[l].lower() != s[r].lower():
				return False
			l += 1
			r -= 1
		return True

A=Solution()
res=A.isPalindrome_2("A man,.<><><><><><> a plan, a canal: Panama")
print(res)
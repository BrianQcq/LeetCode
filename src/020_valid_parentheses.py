"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

Input: "()"
Output: true

Input: "()[]{}"
Output: true

Input: "(]"
Output: false

Input: "([)]"
Output: false

Input: "{[]}"
Output: true
"""

class Solution(object):
	def isValid(self, s):
		ref = ["()", "[]", "{}"]
		temp = ["#"]
		for item in s:
			temp.append(item)
			if temp[-2] + temp[-1] in ref:
				temp.pop()
				temp.pop()
		return temp == ["#"]

A=Solution()
res=A.isValid("{{[]([()])}}")
print(res)
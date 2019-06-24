"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.
"""

"""
KEY POINT:
split() is splitting parenthese by default.
"a ".split() ---> ['a']

"a ".split(" ") ---> ['a', '']
"""

class Solution(object):
	def lengthOfLastWords(self,s):
		if len(s) == 0:
			return 0
		temp = s.split()
		if len(temp) == 0:
			return 0
		return len(temp[-1])

A=Solution()
res=A.lengthOfLastWords("a ")
print(res)
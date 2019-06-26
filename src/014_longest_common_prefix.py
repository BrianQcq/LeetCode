"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Input: ["flower","flow","flight"]
Output: "fl"

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution(object):
	def longestCommonPrefix(self, s):
		if not s:
			return ""
		shortest = min(s, key=len)
		# it can be optimized to shortest = s.sort(key=len)[0]
		# because to find the min takes O(n), sort takes O(log n)
		for i, char in enumerate(shortest):
			for other in s:
				if other[i] != char:
					return shortest[:i]
		return shortest


A=Solution()
res=A.longestCommonPrefix(['a','ab'])
print(res)
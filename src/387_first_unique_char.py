
class Solution(object):

	def firstUniqueChar(self, s):
		ref = {}
		for char in s:
			if char in ref:
				ref[char] = 1
			else:
				ref[char] += 1

		for i in range(len(s)):
			if ref[s[i]] == 1:
				return i
		return -1
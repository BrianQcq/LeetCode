import collections
import bisect

class Solution(object):

	def isSubseq(self, s, t):
		i = j = 0
		while i < len(s) and j < len(t):
			if s[i] == t[j]:
				i += 1
			j += 1
		return i == len(s)

# binary search Solution
class Sol(object):

	def createMap(self, s):
		posMap = collections.defaultdict(list)
		for i, char in enumerate(s):
			posMap[char].append(i)
		return posMap

	def isSubSeq(self, s, t):
		start = 0
		posMap = self.createMap(t)
		for char in s:
			if char not in posMap:
				return False
			charIndexList = posMap[char]
			i = bisect.bisect_left(charIndexList, start)
			if i == len(charIndexList):
				return False
			start = charIndexList[i] += 1
		return True
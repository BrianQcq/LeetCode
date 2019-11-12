
class Solution(object):
	def isOneDistance(self, s, t):
		if len(s) > len(t):
			return self.isOneDistance(t, s)
		if len(t) - len(s) > 1 or len(s) == len(t):
			return False
		for i in range(len(s)):
			if s[i] != t[i]:
				return s[i+1:] == t[i+1:] or s[i:] == t[i+1]
		return True
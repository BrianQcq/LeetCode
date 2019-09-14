
class Solution(object):

	def isIso(self, s, t):
		return [s.find(i) for i in s] == [t.find(j) for j in t]

	def isIso_2(self, s, t):
		return len(set(zip(s, t))) == len(set(s)) == len(set(t))
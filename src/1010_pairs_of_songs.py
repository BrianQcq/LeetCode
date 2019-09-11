
class Solution(object):

	def numPairs(self, time):
		ref = [0] * 60
		res = 0
		for i in time:
			res += ref[(600-i)%60]
			ref[i%60] += 1
		return res
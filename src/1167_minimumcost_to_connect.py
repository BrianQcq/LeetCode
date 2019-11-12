from heapq import *

class Solution(object):

	def connectionSticks(self, sticks):
		res = 0
		if len(sticks) == 1:
			return res

		heapify(sticks)
		while len(sticks) >= 2:
			a, b = heappop(sticks), heappop(sticks)
			res += a + b
			heappush(sticks, a + b)
		return res
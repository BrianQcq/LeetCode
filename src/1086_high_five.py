from heapq import *
from collections import defaultdict

class Solution(object):

	def highFive(self, items):
		
		ref = defaultdict(list)

		for idx, val in items:
			heappush(ref[idx], val)
			if len(ref[idx]) > 5:
				heappop(ref[idx])

		res = [[i, sum(ref[i])//len(ref[i])] for i in sorted(ref)]
		return res

A=Solution()
res=A.highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]])
print(res)
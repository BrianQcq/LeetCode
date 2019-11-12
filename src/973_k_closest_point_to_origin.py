from heapq import *


class Solution(object):
	def kClosest(self, points, k):
		q, res = [], []
		for point in points:
			dis = point[0]**2 + point[1]**2
			heappush(q, (dis, point))

		for i in range(k):
			temp = heappop(q)
			res.append(temp[1])
		return res
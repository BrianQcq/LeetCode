import heapq

class Solution(object):

	def lastStoneWeight(self, stones):
		pq = [-x for x in stones]
		heapq.heapify(pq)
		for i in range(len(pq)-1):
			x,y = -heapq.heappop(pq), -heapq.heappop(pq)
			heapq.heappush(pq, -abs(x-y))
		return -pq[0]

A=Solution()
res=A.lastStoneWeight([2,7,4,1,8,1])
print(res)
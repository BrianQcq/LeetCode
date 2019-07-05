
class Solution(object):

	# DP algo
	def minCost_2(self, costs):
		if not costs:
			return 0

		for i in range(1, len(costs)):
			costs[i][0] += min(costs[i-1][1], costs[i-1][2])
			costs[i][1] += min(costs[i-1][0], costs[i-1][2])
			costs[i][2] += min(costs[i-1][0], costs[i-1][1])
		print (costs)
		return min(costs[-1])

A=Solution()
res=A.minCost_2([[17,2,17],[16,16,5],[14,3,19]])
print(res)
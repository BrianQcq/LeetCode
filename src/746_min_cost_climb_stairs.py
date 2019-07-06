"""
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
"""


class Solution(object):
	def minCost(self, costs):
		if len(costs) == 2:
			return min(costs)
		dp = [0] * (len(costs) + 1)
		for i in range(2, len(costs) + 1):
			dp[i] = min(dp[i-1] + costs[i-1], dp[i-2] + costs[i-2])
		return dp[-1]

A=Solution()
res=A.minCost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
print(res)
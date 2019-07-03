"""
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

class Solution(object):

	# DP algo, O(n^2) space
	def minPathSum(self, grid):
		r, c = len(grid), len(grid[0])
		dp = [[1 for x in range(c)] for x in range(r)]
		dp[0][0] = grid[0][0]
		for i in range(1, c):
			dp[0][i] = grid[0][i] + dp[0][i-1]
		for i in range(1, r):
			dp[i][0] = grid[i][0] + dp[i-1][0]
		#print(dp)
		for i in range(1, r):
			for j in range(1, c):
				dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
		#print(dp)
		return dp[-1][-1]


	# Optimized to O(n) space
	def minPathSum_2(self, grid):
		r, c = len(grid), len(grid[0])
		dp = [1 for x in range(c)]
		dp[0] = grid[0][0]
		for i in range(1, c):
			dp[i] = dp[i-1] + grid[0][i]
		for i in range(1, r):
			dp[0] += grid[i][0]
			for j in range(1, c):
				dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
		return dp[-1]

A=Solution()
res=A.minPathSum_2([[1,3,1],[1,5,1],[4,2,1]])
print(res)
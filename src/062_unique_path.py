"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Input: m = 7, n = 3
Output: 28
"""

class Solution(object):

	# recursion, time limit expires

	def uniquePaths(self, m, n):
		if m == 1 or n == 1:
			return 1
		return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)


	# DP algo, O(n^2) space

	def uniquePaths_2(self, m, n):
		table = [[1 for x in range(n)] for x in range(m)]

		for i in range(1, m):
			for j in range(1, n):
				table[i][j] = table[i-1][j] + table[i][j-1]
		return table[m-1][n-1]

	# optimize to O(n) space
	def uniquePaths_3(self, m, n):
		dp = [1] * m
		for i in range(1, n):
			for j in range(1, m):
				dp[j] += dp[j-1]
		return dp[-1]


A=Solution()
res=A.uniquePaths_3(3,3)
print(res)
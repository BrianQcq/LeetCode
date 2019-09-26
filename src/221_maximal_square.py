
class Solution(object):

	def maximalSquare(self, matrix):
		if not matrix:
			return 0
		res = 0
		r, c = len(matrix), len(matrix[0])
		dp = [[0] * (c+1) for i in range(r+1)]

		for i in range(r):
			for j in range(c):
				if matrix[i][j] == '1':
					dp[i+1][j+1] = min(dp[i][j],dp[i][j+1],dp[i+1][j]) + 1
					res = max(res, dp[i+1][j+1] ** 2)
		return res

A=Solution()
res=A.maximalSquare([['1']])
print(res)
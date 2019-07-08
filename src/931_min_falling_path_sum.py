
class Solution(object):
	def minFallPathSum(self, A):
		if not A or not A[0]:
			return 0
		if len(A) == 1:
			return min(A[0])

		for i in range(1, len(A)):
			for j in range(len(A[0])):
				if j == 0:
					A[i][j] += min(A[i-1][j], A[i-1][j+1])
				elif j == len(A[0]) - 1:
					A[i][j] += min(A[i-1][j-1], A[i-1][j])
				else:
					A[i][j] += min(A[i-1][j-1], A[i-1][j], A[i-1][j+1])
		return min(A[-1])



	# optimize O(n) space
	def minFallPathSum_2(self, A):
		dp = A[0]
		for row in A[1:]:
			dp = [value + min([dp[c], dp[max(c - 1, 0)], dp[min(len(A) - 1, c + 1)]]) for c, value in enumerate(row)]
		return min(dp)

A=Solution()
res=A.minFallPathSum_2([[1,2,3],[4,5,6],[7,8,9]])
print(res)
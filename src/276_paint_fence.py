"""
Thoughts and proof:

To paint i-th post:
1. num_ways(i) = num_diff(i) + num_same(i)
2. num_diff(i) = num_ways(i-1) * (k-1)			# To paint i-th post with different color to (i-1)-th
3. num_same(i) = num_diff(i-1)					# To paint i-th post with same color to (i-1)-th

--> num_ways = num_ways(i-1) * (k-1) + num_ways(i-2) * (k-1)
"""


class Solution(object):

	#recursion 
	def numWays(self, n, k):
		if n == 0 or k == 0:
			return 0
		if n <= 2:
			return k**n
		return (self.numWays(n-1, k) + self.numWays(n-2, k)) * (k-1)


	# DP algo
	def numWays_2(self, n, k):
		if n == 0 or k == 0:
			return 0
		if n == 1:
			return k
		dp = [0] * (n+1)
		dp[0] = 0
		dp[1] = k
		dp[2] = k**2
		for i in range(3, n+1):
			dp[i] = (dp[i-1] + dp[i-2]) * (k-1)
		return dp[n]



A=Solution()
res=A.numWays_2(3,3)
print(res)
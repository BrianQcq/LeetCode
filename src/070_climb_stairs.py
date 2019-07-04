"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution(object):

	# recursive, tle problem
	def climbStairs(self, n):
		if n == 1:
			return 1
		if n == 2:
			return 2
		return self.climbStairs(n-1) + self.climbStairs(n-2)


	# DP algo, O(n) space
	def climbStairs_2(self, n):
		if n == 1:
			return 1
		if n == 2:
			return 2
		dp = [1] * n
		dp[1] = 2
		for i in range(2, n):
			dp[i] = dp[i-1] + dp[i-2]
		return dp[-1]

	# DP algo optimized to O(1) space
	def climbStairs_3(self, n):
		dp = [1, 2]
		if n == 1:
			return dp[0]
		if n == 2:
			return dp[1]
		for i in range(2, n):
			dp[0], dp[1] = dp[1], dp[0] + dp[1]
		return dp[1]

A=Solution()
res=A.climbStairs(5)
our=A.climbStairs_3(5)
print(res)
print(our)
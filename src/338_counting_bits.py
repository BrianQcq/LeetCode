
class Solution(object):
	def countBits(self, num):
		dp = [0] * (num+1)
		dp[0] = 0
		dp[1] = 1

		diff = 2
		for i in range(2, num+1):
			if i // diff == 2:
				diff = 2 * diff
			dp[i] = 1 + dp[i-diff]
			#print(i, dp[i])
		#print(dp)
		return dp[-1]
A=Solution()
res=A.countBits(10)
print(res)
# if we have even number of piles, player who takes first move will always win


class Solution(object):

	# even numbe of piles
	def stoneGame(self, piles):
		return True


	# if odd number of piles is allowed, DP algo
	"""
	dp[i][j] means the biggest number of stones you can get more than opponent picking piles in piles[i] ~ piles[j].
	You can first pick piles[i] or piles[j].
	1. If you pick piles[i], your result will be piles[i] - dp[i + 1][j]
	2. If you pick piles[j], your result will be piles[j] - dp[i][j - 1]

	--> dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
	only need to return dp[i][j] > 0
	"""
	def stoneGame_2(self, piles):
		n = len(piles)
		dp = [[0] * n for i in range(n)]
		for i in range(n):
			dp[i][i] = piles[i]
		for x in range(1, n):
			for y in range(n-x):
				dp[y][y+x] = max(piles[y] - dp[y+1][y+x], piles[y+x] - dp[y][y+x-1])
		return dp[0][-1] > 0


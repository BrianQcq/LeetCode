
class Solution(object):

	def maxProfit(self, prices):
		if not prices:
			return 0

		num = 2
		dp = [[0 for i in range(len(prices))] for j in range(num+1)]

		for k in range(1, num+1):
			for i in range(1, len(prices)):
				max_profit = max(0, prices[i] - prices[0])
				for j in range(1, i):
					max_profit = max(max_profit, prices[i]-prices[j]+dp[k-1][j-1])
				dp[k][i] = max(dp[k][i-1], max_profit)
		return dp[-1][-1]

	def maxProfit_2(self, prices):
		if not prices:
			return 0

		num = 2
		dp = [[0 for i in range(len(prices))] for j in range(num + 1)]

		for k in range(1, num+1):
			min_ = prices[0]
			for i in range(1, len(prices)):
				min_ = min(min_, prices[i] - dp[k-1][i-1])
				dp[k][i] = max(dp[k][i-1], prices[i] - min_)
		return dp[-1][-1]

	def maxProfit_3(self, prices):

		lowest = float('inf')
		diff = -float('inf')
		onebuy = twobuy = 0

		for price in prices:
			lowest = min(lowest, price)
			onebuy = max(onebuy, price - lowest)

			diff = max(diff, onebuy - price)
			twobuy = max(twobuy, price + diff)
		return twobuy

	def maxProfit_4(self, prices):

		if not prices:
			return 0
		num = 2
		dp = [[0 for i in range(len(prices))] for j in range(num+1)]

		for k in range(1, num+1):
			max_diff = -prices[0]
			for i in range(1, len(prices)):
				if i > 1:
					max_diff = max(max_diff, dp[k-1][i-1] - prices[i])
				dp[k][i] = max(dp[k][i-1], max_diff + prices[i])
		print(dp[-1])
		return dp[-1][-1]

A=Solution()
res=A.maxProfit_4([3,3,5,0,0,3,1,4])
print(res)
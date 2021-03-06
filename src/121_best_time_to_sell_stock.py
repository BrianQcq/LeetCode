"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

class Solution(object):
	def maxProfit(self, prices):
		#if len(prices) < 1:
		#	return 0
		if not prices:
			return 0
		min_price, max_profit = prices[0], 0
		for price in prices[1:]:
			min_price = min(price, min_price)
			max_profit = max(max_profit, price - min_price)
		return max_profit

A=Solution()
res=A.maxProfit([])
print(res)
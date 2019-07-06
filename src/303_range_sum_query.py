
class NumArray(object):
	def __init__(self, nums):

		self.dp = nums[:]
		for i in range(1, len(self.dp)):
			self.dp[i] += self.dp[i-1]


	def sumRange(self, i, j):

		if i > 0:
			return self.dp[j] - self.dp[i-1]
		return self.dp[j]

A=NumArray([-2, 0, 3, -5, 2, -1])
print(A.sumRange(0, 2))
print(A.sumRange(2, 5))
print(A.sumRange(0, 5))
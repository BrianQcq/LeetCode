
class Solution(object):

	def productExceptSelf(self, nums):
		n = len(nums)
		L, R, res = [0]*n, [0]*n, [0]*n

		L[0] = 1
		for i in range(1, n):
			L[i] = L[i-1] * nums[i-1]
		R[-1] = 1
		for j in range(n-2, -1, -1):
			R[j] = R[j+1] * nums[j+1]

		for i in range(n):
			res[i] = L[i] * R[i]
		return res
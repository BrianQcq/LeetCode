"""
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution(object):

	#In place dynamic programming solution, use the element in array to store the global max until its position.
	def maxSubArray(self, nums):
		for i in range(1,len(nums)):
			if nums[i-1] > 0:
				nums[i] += nums[i-1]
		return max(nums)

	def maxSubArray_2(self, nums):
		if max(nums) < 0:
			return max(nums)
		global_max, local_max = 0, 0
		for i in nums:
			local_max = max(0, local_max + i)
			global_max = max(global_max, local_max)
		return global_max




A=Solution()
res=A.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(res)
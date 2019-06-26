"""
Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution(object):
	def threeSumClosest(self, nums, target):
		nums.sort()
		res = sum(nums[:3])
		for i in range(len(nums) - 2):
			l, r = i + 1, len(nums) - 1
			while l < r:
				s = nums[i] + nums[l] + nums[r]
				if abs(target - s) < abs(target - res):
					res = s
				if s < target:
					l += 1
				elif s > target:
					r -= 1
				else:
					return res
		return res


A=Solution()
res=A.threeSumClosest([0,3,8,-1,24,26],22)
print(res)
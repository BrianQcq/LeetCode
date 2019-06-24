"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):

	#Brute force solution, time complexity O(n^2)
	def twoSum(self, nums, target):
		for i in range(len(nums)):
			for j in range(i+1,len(nums)):
				if nums[i] + nums[j] == target:
					return [i,j]

	#If sorted array, two pointers method, time complexity O(n)
	#Wrong Answer
	def twoSum_2(self, nums, target):
		left,right = 0,len(nums) - 1
		temp_sum = nums[left] + nums[right]
		while temp_sum != target:
			if temp_sum < target:
				left += 1
				temp_sum = nums[left] + nums[right]
			if temp_sum > target:
				right -= 1
				temp_sum = nums[left] + nums[right]
		return [left,right]

	#Hash table solution, time complexity O(n)
	def twoSum_3(self, nums, target):
		if len(nums) <= 1:
			return False
		buff_dict = {}
		for i in range(len(nums)):
			if nums[i] in buff_dict:
				return [buff_dict[nums[i]], i]
			else:
				buff_dict[target - nums[i]] = i


A=Solution()
res=A.twoSum_3([2,7,11,15],22)
print(res)
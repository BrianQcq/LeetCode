"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

class Solution(object):
	def searchRange(self, nums, target):
		if not nums:
			return [-1,-1]

		low, high = 0, len(nums) - 1
		res = [-1,-1]
		while low < high:
			mid = (low + high)//2
			if nums[mid] < target:
				low = mid + 1
			else:
				high = mid
		if nums[low] != target:
			return res
		else:
			res[0] = low
			#print(res)

		high = len(nums) - 1

		while low < high:
			mid = (low + high)//2 + 1
			#print(mid)
			if nums[mid] > target:
				high = mid -1 
			else:
				low = mid

		res[1] = high

		return res


A=Solution()
res=A.searchRange([5,7,7,8,8,10],7)
print(res)
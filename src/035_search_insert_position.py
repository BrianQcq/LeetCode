"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Input: [1,3,5,6], 5
Output: 2

Input: [1,3,5,6], 2
Output: 1

Input: [1,3,5,6], 7
Output: 4

Input: [1,3,5,6], 0
Output: 0
"""

class Solution(object):

	#Naive solution, time complexity O(n)
	def searchInsert(self, nums, target):
		for i in range(len(nums)):
			if nums[i] >= target:
				return i
		return len(nums)

	#Binary search solution, time complextity O(log n)
	def searchInsert_2(self, nums, target):
		left, right = 0, len(nums) - 1
		while left <= right:
			mid = (left + right) // 2
			if nums[mid] == target:
				return mid
			elif nums[mid] < target:
				left = mid + 1
			else:
				right = mid - 1
		return left

A=Solution()
res=A.searchInsert_2([8,12,16,24,32,65,78,98],31)
print(res)
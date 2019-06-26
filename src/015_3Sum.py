"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

The solution set must not contain duplicate triplets.

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution(object):

	# time limit still expires. not optimal solution
	def threeSum(self, nums):
		res = []
		nums.sort()
		#print(nums)

		for i in range(len(nums) - 2):
			l, r = i+1, len(nums)-1
			while l < r:
				temp_sum = nums[i] + nums[l] + nums[r]
				#print(temp_sum)
				if temp_sum == 0:
					if sorted([nums[i],nums[l],nums[r]]) not in res:
						res.append([nums[i],nums[l],nums[r]])
					l += 1
					r -= 1
				elif temp_sum < 0:
					l += 1
				else:
					r -= 1
		return res


	# time limit expires resolved, time complexity O(n^2)
	def threeSum_2(self, nums):
		res = []
		nums.sort()
		for i in range(len(nums) - 2):
			if i > 0 and nums[i] == nums[i-1]:
				continue
			l, r = i+1, len(nums)-1
			while l < r:
				s = nums[i] + nums[l] + nums[r]
				if s < 0:
					l += 1
				elif s > 0:
					r -= 1
				else:
					res.append((nums[i], nums[l], nums[r]))
					while l < r and nums[l] == nums[l+1]:
						l += 1
					while l < r and nums[r] == nums[r-1]:
						r -= 1
					l += 1
					r -= 1
		return res


A=Solution()
res=A.threeSum_2([-1,0,1,2,-1,-4])
print(res)
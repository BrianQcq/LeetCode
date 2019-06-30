"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

class Solution(object):
	def fourSum(self, nums, target):
		nums.sort()
		results = []
		self.findNSum(nums, target, 4, [], results)
		return results

	def findNSum(self, nums, target, N, result, results):
		#print(nums)
		if len(nums) < N or N < 2:
			return

		# two-pointer 2 sum
		if N == 2:
			l, r = 0, len(nums) - 1
			while l < r:
				s = nums[l] + nums[r]
				if s == target:
					results.append(result + [nums[l], nums[r]])
					l += 1; r -= 1
					while l < r and nums[l] == nums[l+1]:
						l += 1
					while l < r and nums[r] == nums[r-1]:
						r -= 1
				elif s < target:
					l += 1
				else:
					r -= 1
		else:
			for i in range(0, len(nums)-N+1):
				if target < nums[i]*N or target > nums[-1]*N:
					break
				if i == 0 or (i > 0 and nums[i-1] != nums[i]):
					self.findNSum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
		return


A=Solution()
res=A.fourSum([-1,0,-5,-2,-2,-4,0,1,-2], -9)
res2=A.fourSum([0,0,0,0],0)
print(res)
print(res2)



# optimized version, using pointers instead of slicing. time complexity of slicing: O(n) worst case
class Solution2(object):
	def fourSum(self, nums, target):
		def findNSum(l, r, target, N, result, results):
			if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:
				return

			if N == 2:
				while l < r:
					s = nums[l] + nums[r]
					if s == target:
						results.append(result + [nums[l], nums[r]])
						l += 1
						while l < r and nums[l] == nums[l-1]:
							l += 1
					elif s < target:
						l += 1
					else:
						r -= 1
			else:
				for i in range(l, r + 1):
					if i==l or (i > l and nums[i-1] != nums[i]):
						findNSum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

		nums.sort()
		results = []
		findNSum(0, len(nums)-1, target, 4, [], results)
		return results


B=Solution2()
Bres = B.fourSum([-1,0,-5,-2,-2,-4,0,1,-2], -9)
print(Bres)
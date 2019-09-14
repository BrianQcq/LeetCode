
class Solution(object):

	def checkPossible(self, nums):
		a = nums[:]
		b = nums[:]

		for i in range(len(nums)-1):
			if nums[i] > nums[i+1]:
				a[i] = nums[i+1]
				b[i+1] = nums[i]
				break
		return a == sorted(a) or b == sorted(b)

	def checkPossible_2(self, nums):
		cnt = 0
		for i in range(1, len(nums)):
			if nums[i-1] > nums[i]:
				cnt += 1
				if i < 2 or nums[i-2] <= nums[i]:
					nums[i-1] = nums[i]
				else:
					nums[i] = nums[i-1]:
		return cnt <= 1
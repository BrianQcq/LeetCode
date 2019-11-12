
class Solution(object):

	# two pass
	def sortArrayByParity(self, nums):
		even = [i for i in nums if i%2 == 0]
		odd = [j for j in nums if j%2 == 1]
		return even + odd

	# one pass
	def sortArrayByParity_2(self, nums):
		l, r = 0, len(nums) - 1
		while l < r:
			if nums[l]%2 > A[r]%2:
				nums[l], nums[r] = nums[r], nums[l]
			if nums[l]%2 == 0:
				l += 1
			elif nums[r]%2 == 1:
				r -= 1
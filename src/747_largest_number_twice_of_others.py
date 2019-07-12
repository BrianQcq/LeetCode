class Solution(object):

	def dominantIndex(self, nums):
		num_max = max(nums)
		flag = True
		for i in range(len(nums)):
			if nums[i] != num_max:
				if nums[i] * 2 > num_max:
					flag = False
		if flag:
			return nums.index(num_max)
		return -1


	def dominantIndex_2(self, nums):
		m = max(nums)
		if all(m >= 2 * x for x in nums if x != m):
			return nums.index(m)
		return -1


A=Solution()
res=A.dominantIndex([1,2,6,3,3,0,2])
print(res)
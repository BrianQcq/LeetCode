
class Solution(object):

	def subarraySum(self, nums, k):

		count, res, cur = {0: 1}, 0, 0
		for num in nums:
			cur += num
			res += count.get(cur-k, 0)
			count[cur] = count.get(cur, 0) + 1
		return res

A=Solution()
res=A.subarraySum([1,1,1],2)
print(res)
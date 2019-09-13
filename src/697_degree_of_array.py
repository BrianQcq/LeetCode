import collections

class Solution(object):

	def findShortest(self, nums):
		nums_map, deg, min_len = collections.defaultdict(list), 0, float('inf')
		for i, num in enumerate(nums):
			nums_map[num].append(i)
			deg = max(deg, len(nums_map[num]))

		for num, idxs in nums_map.items():
			if len(idxs) == deg:
				min_len = min(min_len, idxs[-1]-idxs[0]+1)
		return min_len


A=Solution()
res=A.findShortest([1, 1, 2, 2, 2, 3, 1])
print(res)
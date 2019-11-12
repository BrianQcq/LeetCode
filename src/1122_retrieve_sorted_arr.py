from collections import defaultdict


class Solution(object):

	def retriveSortedArray(self, arr1, arr2):
		arr1.sort()
		ref = set(arr2)
		lookup = defaultdict(list)
		res = []
		for val in arr1:
			if val in ref:
				lookup[val].append(val)
			else:
				lookup['other'].append(val)
		for val in arr2:
			res += lookup[val]
		res += lookup['other']
		return res
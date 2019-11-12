from collections import defaultdict

class Solution(object):

	def groupAnagram(self, strs):
		ref = defaultdict(list)
		for item in strs:
			ref[tuple(sorted(item))].append(item)
		return ref.values()
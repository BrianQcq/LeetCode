from collections import defaultdict

class Solution(object):

	def longestPalin(self, s):
		res = 0
		ref = defaultdict(int)
		for char in s:
			ref[char] += 1
		for key, val in ref.items():
			a, b = divmod(val, 2)
			res += 2 * a
			ref[key] = b

		res = res + 1 if any(val%2 == 1 for val in ref.values()) else res
		return res

class Solution(object):

	# brute force
	def trap(self, height):
		res = 0
		for i in range(len(height)):
			maxl = maxr = 0
			for l in range(i+1):
				maxl = max(maxl, height[l])
			for r in range(i, len(height)):
				maxr = max(maxr, height[r])
			res += min(maxl, maxr) - height[i]
		return res

	# 2-pointers
	def trap_2(self, height):
		l, r = 0, len(height) - 1
		res = 0
		maxl = maxr = 0

		while l <= r:
			if height[l] <= height[r]:
				if height[l] >= maxl:
					maxl = height[l]
				else:
					res += maxl - height[l]
				l += 1
			else:
				if height[r] >= maxr:
					maxr = height[r]
				else:
					res += maxr - height[r]
				r -= 1
		return res
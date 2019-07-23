def guess(num):
	pass


class Solution(object):
	def guess(self, n):
		l, r = 1, n
		while l < r:
			mid = (l + r)//2
			if guess(mid) == 1:
				l = mid + 1
			else:
				r = mid
		return l
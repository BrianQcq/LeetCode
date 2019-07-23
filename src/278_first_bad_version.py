
def isBadVersion(self, n):
	pass

class Solution(object):

	def firstBadVer(self, n):
		l, r = 0, n
		while l < r:
			mid = (l + r)//2
			if not isBadVersion(mid):
				l = mid + 1
			else:
				r = mid
		return l


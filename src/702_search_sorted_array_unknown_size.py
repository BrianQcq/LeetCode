
class Solution(object):
	def search(self, reader, target):
		r = 1
		while reader.get(r) < target:
			r *= 2
		l = r // 2
		while l <= r:
			mid = (l+r)//2
			if reader.get(mid) == target:
				return mid
			if reader.get(mid) < target:
				l = mid + 1
			else:
				r = mid - 1
		return -1
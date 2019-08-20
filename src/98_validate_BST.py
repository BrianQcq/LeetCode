
class Solution(object):
	def isValid(self, root, lo=float('-inf'), hi=float('inf')):
		if not root:
			return True
		if root.val <= lo or root.val >= hi:
			return False
		return self.isValid(root.left, lo, min(root.val, hi)) and self.isValid(root.right, max(lo, root.val), hi)

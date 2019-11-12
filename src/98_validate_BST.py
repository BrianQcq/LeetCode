
class Solution(object):

	def isValidBST(self, root, lo = -float('inf'), hi = float('inf')):
		if not root:
			return True
		if root.val >= hi or root.val <= lo:
			return False
		return self.isValidBST(root.left, lo, root.val) and self.isValidBST(root.right, root.val, hi)
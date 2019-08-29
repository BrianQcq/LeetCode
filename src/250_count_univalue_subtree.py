
class Solution(object):

	def countSubtree(self, root):
		self.count = 0
		self.checkUni(root)
		return self.count

	def checkUni(self, node):
		if not node:
			return True
		l, r = self.checkUni(node.left), self.checkUni(node.right)
		if l and r and (not node.left or node.left.val == node.val) and (not node.right or node.right.val == node.val):
			self.count += 1
			return True
		return False
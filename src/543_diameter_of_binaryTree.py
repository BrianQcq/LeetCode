# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	diameter = 0

	def diameterOfBinaryTree(self, root):
		if not root:
			return 0
		l = self.dep(root.left)
		r = self.dep(root.right)
		self.diameter = max(self.diameter, l+r)
		self.diameterOfBinaryTree(root.left)
		self.diameterOfBinaryTree(root.right)
		return self.diameter

	def dep(self, node):
		if not node:
			return 0
		return 1 + max(self.dep(node.left), self.dep(node.right))


class Solution_2(object):

	def diameterOfBinaryTree(self, root):
		self.res = 1
		def depth(node):
			if not node:
				return 0
			l = depth(node.left)
			r = depth(node.right)
			self.res = max(self.res, l+r+1)
			return max(l, r) + 1

		depth(root)
		return self.res - 1
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

	def convert(self, root):
		total = 0
		cur = root
		stack = []
		while True:
			while root:
				stack.append(root)
				root = root.right
			if not stack:
				return cur
			node = stack.pop()
			node.val, total = node.val + total, node.val + total
			root = node.left


class Solution_2(object):

	def __init__(self):
		self.total = 0

	def convertBST(self, root):
		if root:
			self.convertBST(root.right)
			self.total += root.val
			root.val = self.total
			self.convertBST(root.left)
		return root
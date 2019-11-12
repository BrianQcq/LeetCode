# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

	def invert(self, root):
		if not root:
			return None
		if not root.left and not root.right:
			return root
		root.left, root.right = root.right, root.left
		self.invert(root.left)
		self.invert(root.right)
		return root
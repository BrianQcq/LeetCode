# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

	def binaryTreePath(self, root):

		if not root:
			return []

		res = []
		def dfs(node, s):
			if node.left:
				dfs(node.left, s+'->'+str(node.val))
			if node.right:
				dfs(node.right, s+'->'+str(node.val))
			if not node.left and not node.right:
				s += '->' + str(node.val)
				res.append(s[2:])

		dfs(root, '')
		return res
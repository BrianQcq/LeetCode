
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

	def rob(self, root):

		def dfs(node):
			if not node:
				return (0,0)
			l, r = dfs(node.left), dfs(node.right)
			now = node.val + l[1] + r[1]
			later = max(l) + max(r)
			return (now, later)
		res = dfs(root)
		return max(res)
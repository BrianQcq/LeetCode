# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

	def sumRootToLeaf(self, root):
		nums = []

		def dfs(node, s):
			if node.left:
				dfs(node.left, s+str(node.val))
			if node.right:
				dfs(node.right, s+str(node.val))
			if not node.left and not node.right:
				nums.append(s+str(node.val))

		dfs(root, '')
		res = 0
		for num in nums:
			res += int(num, 2)
		return res
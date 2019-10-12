
class Solution(object):
	maxpath = -float('inf')
	def maxPathSum(self, root):

		def maxPathAtNode(tree_node):
			if not tree_node:
				return 0
			left = max(0, maxPathAtNode(tree_node.left))
			right = max(0, maxPathAtNode(tree_node.right))
			self.maxpath = max(self.maxpath, tree_node.val + left + right)
			return tree_node.val + max(left, right)

		if not root:
			return 0
		self.max_path = root.val
		ignore = maxPathAtNode(root)
		return self.max_path
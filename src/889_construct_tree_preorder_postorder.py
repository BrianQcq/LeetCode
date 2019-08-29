
class Solution(object):

	def buildTree(self, pre, post):
		if not pre or not post:
			return None
		root = TreeNonde(pre[0])
		if len(post) == 1:
			return root
		idx = pre.index(post[-2])
		root.left = self.buildTree(pre[1:idx], post[:idx-1])
		root.right = self.buildTree(pre[idx:], post[idx-1:-1])
		return root
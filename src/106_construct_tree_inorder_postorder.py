
class Solution(object):

	def buildTree(self, inorder, postorder):
		if postorder:
			idx = inorder.index(postorder.pop())
			root = TreeNode(inorder[idx])
			root.left = self.buildTree(inorder[0:idx], postorder[0:idx])
			root.right = self.buildTree(inorder[idx+1:], postorder[idx:])
			return root
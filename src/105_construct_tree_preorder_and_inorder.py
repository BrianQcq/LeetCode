
class Solution(object):

	def buildTree(self, preorder, inorder):
		if inorder:
			idx = inorder.index(preorder.pop(0))
			root = TreeNode(inorder[idx])
			root.left = self.buildTree(preorder, inorder[0:idx])
			root.right = self.buildTree(preorder, inorder[idx+1:])
			return root
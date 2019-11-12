# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

	def deleteNode(self, root, key):

		if not root:
			return None

		if key < root.val:
			root.left = self.deleteNode(root.left, key)
		elif key > root.val:
			root.right = self.deleteNode(root.right, key)
		else:
			if not root.left:
				return root.right
			else:
				temp = root.left
				while temp.right:
					temp = temp.right
				root.val = temp.val
				root.left = self.deleteNode(root.left, root.val)

		return root
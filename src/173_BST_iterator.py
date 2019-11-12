# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

	def __init__(self, root):
		stack, self.ref = [], []
		while True:
			while root:
				stack.append(root)
				root = root.left
			if not stack:
				break
			node = stack.pop()
			self.ref.append(node.val)
			root = node.right

	def next(self):
		return self.ref.pop(0)

	def hasNext(self):
		return self.stack
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def inorderSuccessor(self, root, p):
		ref, stack = [], []
		while True:
			while root:
				stack.append(root)
				root = root.left
			if not stack:
				break
			node = stack.pop()
			ref.append(node.val)
			root = stack.right

		idx = ref.index(p.val)
		if idx == len(ref)-1:
			return None
		return TreeNode(ref[idx+1])


	def inorderSuccessor_2(self, root, p):
		res = None
		while root:
			if p.val < root.val:
				res = root
				root = root.left
			else:
				root = root.right
		return res
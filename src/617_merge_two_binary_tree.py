# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

	def mergetTrees(self, t1, t2):
		if not t1 and not t2:
			return None
		if not t1:
			return t2
		if not t2:
			return t1
		t1.val += t2.val
		t1.left = self.mergetTrees(t1.left, t2.left)
		t1.right = self.mergetTrees(t1.right, t2.right)
		return t1
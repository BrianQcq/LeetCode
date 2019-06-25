"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

"""

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def isSymmetric(self, root):
		if not root:
			return True
		return self.isMirrow(root.left, root.right)

	def isMirrow(self, left, right):
		if left is None and right is None:
			return True
		if left is None or right is None:
			return False
		if left.val == right.val:
			inside = self.isMirrow(left.right, right.left)
			outside = self.isMirrow(left.left, right.right)
			return inside and outside
		return False
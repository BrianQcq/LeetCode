# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

	def isCousins(self, root, x, y):

		stack = [root]
		parent = {root.val: 0}
		while x not in parent or y not in parent:
			node = stack.pop(0)
			if node.left:
				parent[node.left.val] = node.val
				stack.append(node.left)
			if node.right:
				parent[node.right.val] = node.val
				stack.append(node.right)

		dep_x = dep_y = 0
		xp, yp = x, y
		while xp:
			dep_x += 1
			xp = parent[xp]
		while yp:
			dep_y += 1
			yp = parent[yp]

		return dep_x == dep_y and parent[x] != parent[y]
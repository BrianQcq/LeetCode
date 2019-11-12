class TreeNode(object):
	def __init__(self, val, left, right, next):
		self.val = val
		self.left = left
		self.right = right
		self.next = next


class Solution(object):

	def connect(self, root):
		if not root:
			return root
		stack = [root]
		while stack:
			next_level = []
			for node in stack:
				if node.left and node.right:
					next_level.extend([node.left, node.right])
			for i in range(len(stack)-1):
				stack[i].next = stack[i+1]
			stack = next_level
		return root
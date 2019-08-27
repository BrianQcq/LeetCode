
class Solution(object):

	def preorder(self, root):
		if not root:
			return []
		stack = [root]
		output = []
		while stack:
			node = stack.pop()
			if node is not None:
				output.append(node.val)
				if node.right is not None:
					stack.append(node.right)
				if node.left is not None:
					stack.append(node.left)
		return output

class Solution(object):

	def postorder(self, root):
		res, stack = [], [(root, False)]
		while stack:
			node, visited = stack.pop()
			if node:
				if visited:
					res.append(node.val)
				else:
					stack.append((node, True))
					stack.append((node.right, False))
					stack.append((node.left, False))
		return res

	def postorder_2(self, root):
		res, stack = [], [root]
		while stack:
			node = stack.pop()
			if node:
				res.append(node.val)
				stack.append(node.left)
				stack.append(node.right)
		return res[::-1]
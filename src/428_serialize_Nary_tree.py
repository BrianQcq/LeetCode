"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Codec(object):

	def serialize(self, root):
		if not root:
			return ''
		res = []

		def preorder(node):
			res.append(str(node.val))
			for child in node.children:
				preorder(child)
			res.append('#')

		preorder(root)
		return res

	def deserialize(self, data):
		if not data:
			return None
		stack = []
		for value in data:
			if value != '#':
				stack.append(Node(int(value), []))
			elif len(stack) >= 2:
				node = stack.pop()
				stack[-1].children.append(node)
		return stack[-1]
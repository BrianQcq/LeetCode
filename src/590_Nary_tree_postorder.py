"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution(object):

	def postorder(self, root):
		stack = [root]
		res = []
		if not root:
			return res

		while stack:
			node = stack.pop()
			if node.children:
				stack.extend(node,children)
			res.append(node.val)
		return res[::-1]
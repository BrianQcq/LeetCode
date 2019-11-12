"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):

	def preorder(self, root):
		if not root:
			return []

		stack = [root]
		res = []
		while stack:
			node = stack.pop()
			if node.children:
				stack.extend(node.children[::-1])
			res.append(node.val)
		return res
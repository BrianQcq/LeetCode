"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""

class Solution(object):

	def inorderSuccessor(self, node):

		if node.right:
			node = node.right
			while node.left:
				node = node.left
			return node

		if node.parent and node.parent == node.right:
			node = node.parent
		return node.parent
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution(object):

	def maxDepth(self, root):

		if not root:
			return 0
		elif root.children == []:
			return 1
		else:
			return max([1+self.maxDepth(child) for child in root.children])
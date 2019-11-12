"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution(object):

	def levelOrder(self, root):
		level, res = [root], []
		if not root:
			return res

		while level:
			temp = []
			next_level = []
			for node in level:
				if node.children:
					next_level.extend(node.children)
			for node in level:
				temp.append(node.val)
			level = next_level
			res.append(temp)
		return res

	def levelOrder_2(self, root):
		level, res = [root], []
		if not root:
			return res

		while level:
			res.append([node.val for node in level])
			level = [child for node in level for child in node.children]
		return res
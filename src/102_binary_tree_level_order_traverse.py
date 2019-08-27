
class Solution(object):

	# BFS Solution
	def levelOrder(self, root):

		if not root:
			return []
		res, level = [], [root]
		while level:
			res.append([node.val for node in level])
			temp = []
			for node in level:
				temp.extend([node.left, node.right])
			level = [i for i in temp if i]
		return res
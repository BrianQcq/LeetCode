# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec(object):

	def serialize(self, root):
		if not root:
			return ''
		q = deque([root])
		res = []
		while q:
			node = q.popleft()
			if node:
				q.extend([node.left, node.right])
			res.append(str(node.val) if node else '#')
		return ','.join(res)

	def deserialize(self, data):
		if not data:
			return None
		nodes = data.split(',')
		root = TreeNode(int(nodes[0]))
		idx = 1
		q = deque([root])
		while q:
			node = q.popleft()
			
			if nodes[idx] != '#':
				node.left = TreeNode(int(nodes[idx]))
				q.append(node.left)
			idx += 1
			if nodes[idx] != '#':
				node.right = TreeNode(int(nodes[idx]))
				q.append(node.right)
			idx += 1
		return root


['1', '3', '5', '#', '6', '#', '#', '2', '#', '4', '#', '#']
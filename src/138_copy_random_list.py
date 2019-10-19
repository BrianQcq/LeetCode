# Definition for a Node.
class Node(object):
	def __init__(self, val, next, random):
		self.val = val
		self.next = next
		self.random = random


class Solution(object):
	def __init__(self):
		self.visited = {}

	def getCloneNode(self, node):
		if node:
			if node in self.visited:
				return self.visited[node]
			else:
				self.visited[node] = Node(node.val, None, None)
				return self.visited[node]
		return None

	def copyRandomList(self, head):
		if not head:
			return head

		old_node = head
		new_node = Node(old_node.val, None, None)
		self.visited[old_node] = new_node

		while old_node is not None:
			new_node.random = self.getCloneNode(old_node.random)
			new_node.next = self.getCloneNode(old_node.next)

			old_node = old_node.next
			new_node = new_node.next
		return self.visited[head]

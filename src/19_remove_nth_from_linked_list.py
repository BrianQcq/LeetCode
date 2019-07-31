class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None


class Solution(object):

	def remove(self, head, n):
		if not head:
			return None
		first = Node(0)
		first.next = head
		pos = cur = first
		for i in range(n):
			pos = pos.next
		while pos.next:
			cur = cur.next
			pos = pos.next
		cur.next = cur.next.next
		return first.next
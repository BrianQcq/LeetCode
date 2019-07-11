
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):

	# iterative
	def reverseList(self, head):
		if not head:
			return None
		prev, cur = None, head
		while cur:
			nex = cur.next
			cur.next = prev
			prev = cur
			cur = nex
		return prev


	# recursive
	def reverseList_2(self, head):
		if not head not head.next:
			return head

		new_head = self.reverseList_2(head.next)
		next_node = head.next
		next_node.next = head
		head.next = None
		return new_head
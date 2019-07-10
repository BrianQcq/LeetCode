class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):

	# recursive
	def swapPairs(self, head):
		if not head or not head.next:
			return head
		n = ListNode(head.next.val)
		head.next = self.swapPairs(head.next.next)
		n.next = head
		return n


	# iterative
	def swapPairs_2(self, head):
		dummy = prev = ListNode(0)
		prev.next = head
		while prev.next and prev.next.next:
			cur = prev.next
			nex = cur.next
			prev.next, cur.next, nex.next = nex, nex.next, cur
			prev = cur
		return dummy.next
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):

	# recursive
	def merge(self, l1, l2):
		if not l1:
			return l2
		if not l2:
			return l1

		if l1.val <= l2.val:
			l1.next = self.merge(l1.next, l2)
			return l1
		else:
			l2.next = self.merge(l1, l2.next)
			return l2


	# iterative
	def merge_2(self, l1, l2):
		dummy = cur = ListNode(0)
		while l1 and l2:
			if l1.val < l2.val:
				cur.next = l1
				l1 = l1.next
			else:
				cur.next = l2
				l2 = l2.next
			cur = cur.next
		cur.next = l1 or l2
		return dummy.next
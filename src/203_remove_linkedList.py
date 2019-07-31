
class Solution(object):

	# iterative
	def remove(self, head, val):

		while head and head.val == val:
			head = head.next
		if not head:
			return None

		cur = head
		while cur and cur.next:
			if cur.next.val == val:
				cur.next = cur.next.next
			else:
				cur = cur.next
		return head


	# recursive
	def remove_2(self, head, val):
		if not head:
			return None
		nxt = self.remove_2(head.next, val)
		if head.val == val:
			return nxt
		head.next = nxt
		return head
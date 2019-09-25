class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):

	def plusOne(self, head):
		
		num = ''
		while head:
			num += str(head.val)
			head = head.next
		final = str(int(num) + 1)

		idx = res = ListNode(0)
		for i in range(len(final)):
			idx.next = ListNode(int(final[i]))
			idx = idx.next
		return res.next
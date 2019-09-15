
class Solution(object):

	def findmiddle(self, head):

		fast = head
		while fast and fast.next:
			fast = fast.next.next
			head = head.next
		return head
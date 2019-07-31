
class Solution(object):

	def oddEvenLists(self, head):
		if not head:
			return None
		odd = head
		ref = even = head.next
		while odd and odd.next and even and even.next:
			#print(odd)
			#print(even)
			odd.next, even.next = odd.next.next, even.next.next
			odd, even = odd.next, even.next
		odd.next = ref
		return head


class Solution(object):

	def nextGreaterElement(self, nums1, nums2):
		mono_stack = []
		nxt = {}
		for num in nums2:
			while mono_stack and mono_stack[-1] < num:
				nxt[mono_stack.pop()] = num

			mono_stack.append(num)

		return[nxt.get(num, -1) for num in nums1]

class Solution(object):

	def find132Pattern(self, nums):
		stack, ref = [], -float('inf')
		for num in nums[::-1]:
			#print(num)
			if num < ref:
				return True
			while stack and stack[-1] < num:
				ref = stack.pop()
			#print(ref)
			stack.append(num)
			#print(stack)
			#print('=======')
		return False

A=Solution()
res=A.find132Pattern([1,6,13,14,15,8,9,10])
print(res)
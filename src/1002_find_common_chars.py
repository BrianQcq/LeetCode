
class Solution(object):

	def commonChars(self, A):
		l1 = list(A[0])
		for i in range(1,len(A)):
			l2 = list(A[i])
			l1_copy = [n for n in l1]
			for j in l1_copy:
				if j not in l2:
					l1.remove(j)
				else:
					l2.remove(j)
		return l1

class Solution(object):

	def sortedSquares(self, A):
		return sorted([i * i for i in A])

	# optimized space complexity
	def sortedSquares_2(self, A):
		A.sort(key=abs)
		for i in range(len(A)):
			A[i] **= 2
		return 

	# optimized time complexity
	def sortedSquares_3(self, A):
		l, r = 0, len(A)-1
		res = []
		while l < r:
			if abs(A[l]) <= abs(A[r]):
				res.append(A[r] ** 2)
				r -= 1
			else:
				res.append(A[l] ** 2)
				l += 1
		return res[::-1]

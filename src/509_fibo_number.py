
class Solution(object):

	# recursive
	def fib(self, N):
		if N == 0:
			return 0
		if N == 1:
			return 1
		return self.fib(N-1) + self.fib(N-2)

	# optimized version
	def fib_2(self, N):
		F = [0, 1]
		for i in range(N-1):
			F[0], F[1] = F[1], F[0]+F[1]
		if N == 0:
			return F[0]
		return F[1]


A=Solution()
res=A.fib_2(35)
print(res)
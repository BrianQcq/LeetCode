
class Solution(object):
	def countPrimes(self, n):

		def isPrime(x):
			if x < 2:
				return False
			for i in range(2, x//2+1):
				if (x%i) == 0:
					return False
			else:
				return True

		count = 0
		for i in range(1, n):
			if isPrime(i):
				count += 1
		return count


	def countPrimes_2(self, n):
		if n <= 2:
			return 0
		ref = [True] * n
		ref[0] = ref[1] = False

		for i in range(2, n):
			if ref[i] == True:
				for j in range(2, (n-1)//i + 1):
					ref[i*j] = False
		return sum(ref)

A=Solution()
res=A.countPrimes(1000)
print(res)


class Solution(object):

	 # BFS solution
	def numSquares(object, n):
		if n <= 3:
			return n
		lst = []
		i = 1
		while i * i <= n:
			lst.append(i*i)
			i += 1
		print(lst)
		cnt = 0
		toCheck = {n}
		while toCheck:
			print(toCheck)
			cnt += 1
			temp = set()
			for x in toCheck:
				for y in lst:
					if x == y:
						return cnt
					if x < y:
						break
					temp.add(x-y)
			toCheck = temp
		return cnt

	# DP solution
	def numSquares_2(self, n):
		# if n <= 3:
		# 	return n
		dp = [2**31] * (n+1)
		dp[0] = 0
		for i in range(1, len(dp)):
			j = 1
			while j*j <= i:
				dp[i] = min(dp[i], dp[i-j*j] + 1)
				j += 1
		return dp[-1]



A=Solution()
res=A.numSquares(12)
print(res)
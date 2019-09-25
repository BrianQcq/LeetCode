
# def maximalCommonality(s):
# 	n = len(s)
# 	common = 0
# 	for i in range(1, n):
# 		ref = {}
# 		for j in range(i):
# 			ref[s[j]] = 0
# 			if s[j] in s[i:]:
# 				ref[s[j]] += 1

# 		if sum(ref.values()) > common:
# 			common = len(ref)
# 	return common
from collections import defaultdict
def maxcom(s):
	dic = defaultdict(int)
	for c in s:
		dic[c] += 1
	ans = 0
	tmp = 0
	#print(dic)
	dic1 = defaultdict(int)
	for c in s:
		dic1[c] += 1
		dic[c] -= 1
		if dic1[c] <= dic[c]:
			tmp += 1
		elif dic1[c] > dic[c] + 1:
			tmp -= 1
		if tmp > ans:
			ans = tmp
	return ans


# print(maxcom('abcdedeara'))
# print(maxcom('abababab'))


def matrixGame(matrix):
	res = []
	for j in range(len(matrix[0])):
		ref = -float('inf')
		for i in range(len(matrix)):
			if matrix[i][j] > ref:
				ref = matrix[i][j]
		res.append(ref)
	max_nums = sorted(res,reverse=True)
	a = sum([max_nums[i] for i in range(len(max_nums)) if i%2 == 0])
	b = sum([max_nums[j] for j in range(len(max_nums)) if j%2 == 1])
	return a-b

#print(matrixGame([[3,7,5,3,4,5],[4,5,2,6,5,4],[7,4,9,7,8,3]]))



def strangeSort(mapping, nums):
	pass
	res = []
	ref = [0] * len(mapping)
	for i, v in enumerate(mapping):
		ref[v] = i
	#print(ref)
	for num in nums:
		temp = ''
		for i in range(len(num)):
			temp += str(ref[int(num[i])])
		res.append(temp)
	print(res)
	print(sorted(res))

#print(strangeSort([2,1,4,8,6,3,0,9,7,5], ['224','4','023','65','83']))


def findRank(scores, k):
	total = [(sum(scores[i]),i) for i in range(len(scores))]
	#print(total)
	ordered = sorted(total,reverse=True)
	#print(total)
	return ordered[k-1][1]


#print(findRank([[79,89,15],[85,89,92],[71,96,88]], 2))


class SpiralSol(object):

	def isprime(self, x):
		if x < 2:
			return False
		for i in range(2, x//2+1):
			if x % i == 0:
				return False
		else:
			return True

	def spiralOrder(self, matrix):
		ret = []
		while matrix:
			ret += matrix.pop(0)
			if matrix and matrix[0]:
				for row in matrix:
					ret.append(row.pop())
			if matrix:
				ret += matrix.pop()[::-1]
			if matrix and matrix[0]:
				for row in matrix[::-1]:
					ret.append(row.pop(0))
		return ret

	def spiralOrderPrime(self, matrix):
		order = self.spiralOrder(matrix)
		res = []
		for num in order:
			if self.isprime(num):
				res.append(num)
		return res

test=SpiralSol()
res=test.spiralOrderPrime([[7,7,3,8,1],[13,5,4,5,2],[9,2,12,3,9],[6,12,1,11,41]])
#print(res)


def stockPrice(stocks):
	n = len(stocks)
	res = []
	for i in range(6,n):
		res.append(format(sum(stocks[i-6:i+1])/7, '.2f'))
	return res

#print(stockPrice([7,8,8,11,9,7,5,6]))
#print(stockPrice([5,5,5,5,5,5,5,6,6]))


def girdGmae(grid, k, rules):
	r, c = len(grid), len(grid[0])
	alive = [[0] * c for in in range(r)]
	neighbors = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

	while k > 1:
		pass
		
from collections import defaultdict

class Solution(object):

	def findOrder(self, numCourses, prerequisites):
		dic = defaultdict(set)
		nei = defaultdict(set)
		for i, j in prerequisites:
			dic[i].add(j)
			nei[j].add(i)
		stack = [i for i in range(numCourses) if not dic[i]]
		res= []

		while stack:
			node = stack.pop()
			res.append(node)
			for i in nei[node]:
				dic[i].remove(node)
				if not dic[i]:
					stack.append(i)
			dic.pop(node)
		return res if not dic else []

A=Solution()
res=A.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
print(res)
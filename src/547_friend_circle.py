
class Solution(object):
	def findNum(self, M):
		seen = [0] * len(M)
		count = 0
		for i in range(len(M)):
			if seen[i] == 0:
				self.dfs(M, seen, i)
				count += 1
		return count

	def dfs(self, M, visited, i):
		for j in range(len(M)):
			if M[i][j] == 1 and visited[j] == 0:
				visited[j] = 1
				self.dfs(M, visited, j)


class Solution_unionFind(object):
	def findNum(self, M):
		parent = [i for i in range(len(M))]

		def union(i,j):
			parent[find(parent[i])] = find(parent[j])

		def find(i):
			if parent[i] != i:
				parent[i] = find(parent[i])
			return parent[i]

		for i, x in enumerate(M):
			for j, y in enumerate(x):
				if y:
					union(i, j)

		return len(set([find(parent[i]) for i in range(len(M))]))
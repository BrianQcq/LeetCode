from collections import defaultdict

class Solution(object):

	# dfs
	def findItinerary(self, tickets):
		targets = defaultdict(list)
		for a, b in sorted(tickets)[::-1]:
			targets[a].append(b)
		route = []
		#print(targets)
		def dfs(airport):
			while targets[airport]:
				dfs(targets[airport].pop())
			route.append(airport)

		dfs('JFK')
		return route[::-1]

	# bfs
	def findItinerary_2(self, tickets):
		targets = defaultdict(list)
		for a, b in sorted(tickets)[::-1]:
			targets[a].append(b)
		#print(targets)
		route, stack = [], ['JFK']
		while stack:
			while targets[stack[-1]]:
				stack.append(targets[stack[-1]].pop())
			route.append(stack.pop())
		return route[::-1]


A=Solution()
res=A.findItinerary_2([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])
print(res)
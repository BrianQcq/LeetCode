
class Solution(object):

	def remove(self, s):

		def dfs(s):
			print(visited)
			mi = calc(s)
			if mi == 0:
				return [s]
			ans = []
			for x in range(len(s)):
				if s[x] in ('(', ')'):
					ns = s[:x] + s[x+1:]
					if ns not in visited and calc(ns) < mi:
						visited.add(ns)
						ans.extend(dfs(ns))
			return ans

		def calc(s):
			a = b = 0
			for c in s:
				a += {'(': 1, ')': -1}.get(c, 0)
				b += a < 0
				a = max(a,0)
			return a + b

		visited = set([s])
		return dfs(s)


class Sol(object):

	# bfs
	def remove(self, s):
		if not s:
			return ['']
		q = [(s, 0)]
		visited = set()
		visited.add(s)
		found = False
		res = []

		while q:
			for i in range(len(q)):
				top, idx = q.pop(0)

				if self.isValid(top):
					found = True
					res.append(top)

				if found:
					continue

				for j in range(idx, len(top)):
					if top[j] != '(' and top[j] != ')':
						continue

					ns = top[:j] + top[j+1:]
					if ns not in visited:
						visited.add(ns)
						q.append((ns, j))
			if found:
				break
		return res

	def isValid(self, s):
		cnt = 0
		for c in s:
			if c == '(':
				cnt += 1
			elif c == ')':
				cnt -= 1
				if cnt < 0:
					return False
		return cnt == 0

B=Solution()
res=B.remove('()())()')
print(res)
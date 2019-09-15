
class Solution(object):

	def backspace(self, S, T):

		def back(x):
			res = []
			for i in x:
				if i != '#':
					res.append(i)
				else:
					res = res[:-1]
			return res

		return back(S) == back(T)
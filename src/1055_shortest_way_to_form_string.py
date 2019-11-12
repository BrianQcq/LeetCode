
class Solution(object):

	def shirtesWay(self, source, target):
		i = j = res = 0
		ref = set(source)
		for char in target:
			if char not in ref:
				return -1

		while j < len(target):
			if i == len(source):
				res += 1
				i = 0
			elif source[i] == target[j]:
				i += 1
				j += 1
			elif source[i] != target[j]:
				i += 1
		return res+1

A=Solution()
res=A.shirtesWay('xyz', 'xzyxz')
print(res)
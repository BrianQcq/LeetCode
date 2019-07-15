
class Solution(object):

	# recursive 
	def addBianray(self, a, b):
		if len(a) == 0:
			return b
		if len(b) == 0:
			return a

		if a[-1] == '1' and b[-1] == '1':
			return self.addBianray(self.addBianray(a[:-1],b[:-1]), '1') + '0'
		elif a[-1] == '0' and b[-1] == '0':
			return self.addBianray(a[:-1],b[:-1]) + '0'
		else:
			return self.addBianray(a[:-1],b[:-1]) + '1'

A=Solution()
res=A.addBianray('1', '0')
print(res)
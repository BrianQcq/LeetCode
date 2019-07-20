
class Solution(object):

	def dailyTemperature(self, T):
		stack = []
		for i, temp in enumerate(T):
			if i == 0:
				stack.append((i, temp))
			else:
				while stack and temp > stack[-1][1]:
					T[stack[-1][0]] = i - stack[-1][0]
					stack.pop()
				stack.append((i, temp))
		#print(stack)
		if stack:
			for item in stack:
				T[item[0]] = 0
		return T

	def dailyTemperature_2(self, T):

		out = [0] * len(T)
		stack = []
		for i, temp in enumerate(T):
			while stack and T[stack[-1]] < temp:
				cur = stack.pop()
				out[cur] = i - cur
			stack.append(i)
			print(stack)
			print(out)
			print('------')
		return out


A=Solution()
res=A.dailyTemperature_2([55,38,53,81,61,93,97,32,43,78])
print(res)
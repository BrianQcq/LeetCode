# 有1分，2分，5分，10分四种硬币，每种硬币数量无限，给定n分钱(n <= 100000)，有多少中组合可以组成n分钱？

def money(n):
	v = [1, 2, 5, 10]
	dp = [0 for i in range(n+1)]
	dp[0] = 1

	for i in range(len(v)):
		for j in range(v[i], len(dp)):
			dp[j] += dp[j - v[i]]
	return dp[-1]


print(money(1))



# 1. 三个同样的字母连在一起，一定是拼写错误，去掉一个的就好啦：比如 helllo -> hello
# 2. 两对一样的字母（AABB型）连在一起，一定是拼写错误，去掉第二对的一个字母就好啦：比如 helloo -> hello
# 3. 上面的规则优先“从左到右”匹配，即如果是AABBCC，虽然AABB和BBCC都是错误拼写，应该优先考虑修复AABB，结果为AABCC

def WangDachui():
	n = int(input())
	while n > 0:
		s = input()
		res = []
		for char in s:
			if len(res) < 2:
				res.append(char)
				continue
			if len(res) >= 2:
				if char == res[-1] and char == res[-2]:
					continue
			if len(char) >= 3:
				if char == res[-1] and res[-2] == res[-3]:
					continue
			res.append(char)
		print("".join(res))
		n -= 1



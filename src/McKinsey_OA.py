
def trap_rain_water(height):
	# 2-pointer

	l, r = 0, len(height)-1
	res = 0
	maxl = maxr = 0
	while l <= r:
		if height[l] <= height[r]:
			if height[l] >= maxl:
				maxl = height[l]
			else:
				res += maxl - height[l]
			l += 1
		else:
			if height[r] >= maxr:
				maxr = height[r]
			else:
				res += maxr - height[r]
			r -= 1
	return res
#print(trap_rain_water([3,1,1,2,3]))


def fizzBuzz(n):
	res = []
	for i in range(1, n+1):
		if i%5 == 0 and i%3 == 0:
			res.append('FizzBuzz')
		elif i%3 == 0:
			res.append('Fizz')
		elif i%5 == 0:
			res.append('Buzz')
		else:
			res.append(str(i))
	return res
#print(fizzBuzz(15))



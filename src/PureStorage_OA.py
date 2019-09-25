
# Lock Use Analysis

def isLegal(locks):
	cache = set()
	stack = []
	for i, event in enumerate(locks):
		op, lock_id = event.split()
		if op == 'ACQUIRE':
			if lock_id in cache:
				return i + 1
			else:
				cache.add(lock_id)
				stack.append(lock_id)
		else:
			if not stack or stack.pop() != lock_id:
				return i + 1
			else:
				cache.remove(lock_id)
	return 0 if not stack else len(locks) + 1



def numberScore(num):
	res = total = 0
	str_num = str(num)
	for digit in str_num:
		if digit == '7':
			res += 1
		elif int(digit) % 2 == 0:
			res += 4
		total += int(digit)

	if total % 3 == 0:
		res += 2

	step = 1
	for i in range(len(str_num)-1):
		if int(str_num[i]) != int(str_num[i+1]) + 1:
			if step != 1:
				res += step ** 2
			step = 1
		else:
			step += 1
	if step != 1:
		res += step ** 2

	idx = 0
	for i in range(len(str_num)):
		if str_num[i] == '5':
			idx += 1
		else:
			if idx >= 2:
				res += 3 + 2 * (idx - 2) * 3
				idx = 0
			else:
				idx = 0
	if idx != 0:
		res += 3 + 2 * (idx - 2) * 3


	return res


print(numberScore(7162371624871623871))
print(numberScore(5555))
print(numberScore(555))
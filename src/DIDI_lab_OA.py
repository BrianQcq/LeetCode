
def insertFive(num):

	if num >= 0:
		pos = 1
		ref = str(num * pos)
		cur_max = -float('inf')
		for i in range(len(ref)+1):
			temp = ref[:i] + '5' + ref[i:]
			if int(temp) > cur_max:
				cur_max = int(temp)
		return cur_max * pos
	else:
		pos = -1
		ref = str(num * pos)
		cur_max = float('inf')
		for i in range(len(ref)+1):
			temp = ref[:i] + '5' + ref[i:]
			if int(temp) < cur_max:
				cur_max = int(temp)
		return cur_max * pos

#print(insertFive(9954))



def longestContStr(strs):
	max_len = 0
	for i in range(len(strs)):
		temp = strs[i]
		for j in range(len(strs)):			
			if not set(temp) & set(strs[j]):
				temp += strs[j]
		max_len = max(max_len, len(temp))
	return max_len



print(longestContStr(['abc','cba','def','gha','gi']))
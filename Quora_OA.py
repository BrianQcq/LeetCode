# 1. Find how many numbers have even digit in a list.
# Ex.
# Input: A = [12, 3, 5, 3456]
# Output: 2
def evendigit(nums):
	count = 0
	for num in nums:
		if count % 2 == 0:
			count += 1
	return count


# 2. Find the most common elements in a list.
# Ex.
# Input: A = [2, 2, 3, 3, 5]
# Output: [2, 3]
def mostCommon(nums):
	pass
	ref = {}
	max_freq = 0
	for num in nums:
		if num not in ref:
			ref[num] = 1
		ref[num] += 1
		if ref[num] > max_freq:
			max_freq = ref[num]
	res = []
	for num, freq in ref.items():
		if freq == max_freq:
			res.append(num)
	return res

print(mostCommon([2,2,2,2,3,1,3,3,4,3]))


# 3. If two strings are close enough.
# Given two rules to define two strings are cl‍‍‌‌‍‍‌‍‌‍‌‍‍‌‌‍‌‌‌ose enough.
# 1. you can swap neighbor char any times. Ex. "abb" -> "bba"
# 2. If two strings have the same character, then you can change the character into another.
#     Ex. If both strings contain "a" and "b", you can change all "a"s in the first string or change all "b"s in the first string. same as the second string

# Ex.
# Input: S1 = "babzccc", S2 = "abbzczz"
# Output: True
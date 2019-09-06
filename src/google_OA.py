# Number of Steps to Water Plants

# Input: plants = [2, 4, 5, 1, 2], capacity = 6
# Output: 17
# Explanation:
# First you water plants[0] and plants[1] (2 steps).
# Then you have to go back to refill (2 steps) and water plants[2] and plants[3] (4 steps).
# Then again you have to refill (4 steps) and water plants[4] (5 steps).
# So 2 + 2 + 4 + 4 + 5 = 17.

def numStep(plants, capacity):
	if capacity < max(plants):
		return -1
	cap = capacity
	steps = 0
	for i in range(len(plants)):
		if plants[i] <= cap:
			cap -= plants[i]
		else:
			steps += 2 * i
			cap = capacity - plants[i]
		steps += 1

	return steps

# plants = [2, 5, 2, 1, 2]
# capacity = 6
plants = [2, 2, 2, 2]
capacity = 6
print(numStep(plants, capacity))


# Given 2 arrays a and b, each containing n integers. 
# You can swap elements at the same index. 
# Return the minimum number of swaps needed for all elements in either a or b 
# to be the same or -1 if that is not possible.
# 
# Input:
# a = [1, 2, 3, 6, 3, 2]
# b = [2, 1, 2, 2, 2, 4]

# Output: 2

# Explanation:
# You can swap elements at index 1 and 5, so that all elements in b will be equal to 2.
# a = [1, 1, 3, 6, 3, 4]
# b = [2, 2, 2, 2, 2, 2]

def minSwap(A, B):
	# Greedy Approach, A[:] equals to A[0] or B[:] equals to B[0] otherwise -1
	def check(x):
		rotation_a = rotation_b = 0
		for i in range(n):
			if A[i] != x and B[i] != x:
				return -1
			if A[i] != x:
				rotation_a += 1
			elif B[i] != x:
				rotation_b += 1
		return min(rotation_a, rotation_b)

	n = len(A)
	rotations = check(A[0])
	if rotations != -1:
		return rotations
	else:
		return check(B[0])

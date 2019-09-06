# 532. K-diff Pairs in an Array
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.

def findPairs(nums, k):
	nums.sort()
	count = []
	ref = {}
	for i in range(len(nums)):
		if nums[i] in ref:
			count.append((ref[nums[i]],nums[i]))
		ref[nums[i] + k] = nums[i]
	return len(set(count))

# 256. Paint House
# Input: [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
# Minimum cost: 2 + 5 + 3 = 10.

def mincost(costs):
	if not costs:
		return 0
	for i in range(1, len(costs)):
		costs[i][0] += min(costs[i-1][1],costs[i-1][2])
		costs[i][1] += min(costs[i-1][0],costs[i-1][2])
		costs[i][2] += min(costs[i-1][1],costs[i-1][2])
	return min(costs[-1])

house = [[17,2,17],[16,16,5],[14,3,19]]
print(mincost(house))
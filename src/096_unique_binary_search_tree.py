"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""



"""
Thoughts:
1. G(n) --> num of unique bst for storing 1~n
2. F(i, n) --> num of unique bst for i at root, values 1~n
Since:

G(n) = F(1,n) + F(2,n) + F(3,n) +...+ F(n,n)    while
F(i,n) = G(i-1) * G(n-1)

--> G(n) = G(0)*G(n-1) + G(1)*G(n-2) +...+ G(n-1)*G(0)

"""
class Solution(object):
	def numTrees(self, n):
		G = [0] * (n+1)
		G[0] = G[1] = 1

		for i in range(2, n+1):
			for j in range(1, i+1):
				G[i] += G[j-1] * G[i-j]
		return G[-1]

A=Solution()
res=A.numTrees(4)
print(res)
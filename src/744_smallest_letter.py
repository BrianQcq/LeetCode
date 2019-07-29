
class Solution(object):
	def nextGreaterLetter(self, letters, target):
		l, r = 0, len(letters)-1
		while l < r:
			mid = (l+r)//2
			if letters[mid] <= target:
				l = mid + 1
			else:
				r = mid
		#return l
		if target < letters[l]:
			return letters[l]
		else:
			if l == len(letters)-1:
				return letters[0]
			else:
				return letters[l+1]

A=Solution()
res=A.nextGreaterLetter(['c','f','j'], 'j')
print(res)
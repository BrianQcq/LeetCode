
class Solution(object):

	# two pointer technique
	def intersect(self, nums1, nums2):
		nums1.sort()
		nums2.sort()
		pt1, pt2 = 0, 0
		out = []

		while True:
			try:
				if nums1[pt1] > nums2[pt2]:
					pt2 += 1
				elif nums1[pt1] < nums2[pt2]:
					pt1 += 1
				else:
					out.append(nums1[pt1])
					pt1 += 1
					pt2 += 1
			except IndexError:
				break

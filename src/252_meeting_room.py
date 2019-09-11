
class Solution(object):

	def attendMeeting(self, intervals):
		intervals = sorted(intervals)
		for i in range(len(intervals)-1):
			if intervals[i][1] > intervals[i+1][0]:
				return False
		return True

class Solution(object):

	def minMeetingRoom(self, intervals):
		room = {}
		intervals = sorted(intervals)

		for i in range(intervals):
			if not room:
				room[1] = intervals[i][1]
			else:
				for j in range(1,len(room)+1):
					if room[j] <= intervals[i][0]:
						room[j] = intervals[i][1]
						break
				else:
					room[len(room) + 1] = intervals[i][1]
		return len(room)
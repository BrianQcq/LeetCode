import collections

class Solution(object):
	def wallsAndGates(self, rooms):
		if not rooms:
			return
		for i in range(len(rooms)):
			for j in range(len(rooms[0])):
				if rooms[i][j] == 0:
					queue = collections.deque([(i-1,j,1),(i+1,j,1),(i,j-1,1),(i,j+1,1)])
					while queue:
						x, y, val = queue.popleft()
						if x < 0 or x >= len(rooms) or y < 0 or y >= len(rooms[0]) or rooms[x][y] <= val:
							continue
						else:
							rooms[x][y] = val
							queue.extend([(x-1,y,val+1),(x+1,y,val+1),(x,y-1,val+1),(x,y+1,val+1)])
		print(rooms)


A=Solution()
res=A.wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]])
print(res)
from collections import defaultdict


class towSum_uniquepair(object):

	def twosum(self, nums, target):
		res, ref = set(), set()
		for num in nums:
			diff = target - num
			if diff in ref:
				temp = (num, diff) if num > diff else (diff, num)
				if temp not in res:
					res.add(temp)
			ref.add(num)
		return len(res)

# testA=towSum_uniquepair()
# resA=testA.twosum([1, 5, 1, 5], 6)
# print(resA)


import collections
class Solution(object):
    def criticalConnections(self, n, connections):
    	for i in range(len(connections)):
    		for j in range(len(connections[0])):
    			connections[i][j] -= 1
    			
        def makeGraph(connections):
			graph = collections.defaultdict(list)
            for conn in connections:
                graph[conn[0]].append(conn[1])
                graph[conn[1]].append(conn[0])
            return graph

        graph = makeGraph(connections)
        connections = set(map(tuple, (map(sorted, connections))))
        print(connections)
        rank = [-2] * n

        def dfs(node, depth):
            if rank[node] >= 0:
                # visiting (0<=rank<n), or visited (rank=n)
                return rank[node]
            rank[node] = depth
            min_back_depth = n
            for neighbor in graph[node]:
                if rank[neighbor] == depth - 1:
                    continue  # don't immmediately go back to parent. that's why i didn't choose -1 as the special value, in case depth==0.
                back_depth = dfs(neighbor, depth + 1)
                if back_depth <= depth:
                    connections.discard(tuple(sorted((node, neighbor))))
                min_back_depth = min(min_back_depth, back_depth)
            rank[node] = n  # this line is not necessary. see the "brain teaser" section below
            return min_back_depth
            
        dfs(0, 0)  # since this is a connected graph, we don't have to loop over all nodes.
        # return list(connections)
        temp = list(connections)
        for i in range(len(temp)):
        	for j in range(len(temp[0])):
        		temp[i][j] += 1
        return temp


# test=Critical_connection()
# res = test.find(5, [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]])
# print(res)
test=Solution()
#res=test.criticalConnections(5, [[0, 1], [0, 2], [2, 3], [0, 3], [3, 4]])
res = test.criticalConnections(5, [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]])
print(res)



class Favourite_genres(object):

	def favGenres(self, userSongs, songGenres):
		output = {}
		for user in userSongs:
			song_list = userSongs[user]
			count = {}

			for song in song_list:
				for genre in songGenres:
					if song in songGenres[genre]:
						count[genre] = count.get(genre, 0) + 1
			output[user] = [key for key,val in count.items() if val == max(count.values())]

		return output

# testC=Favourite_genres()
# userSongs = {  
#        "David": ["song1", "song2", "song3", "song4", "song8"],
#        "Emma":  ["song5", "song6", "song7"]
#     }
# songGenres = {  
#        "Rock":    ["song1", "song3"],
#        "Dubstep": ["song7"],
#        "Techno":  ["song2", "song4"],
#        "Pop":     ["song5", "song6"],
#        "Jazz":    ["song8", "song9"]
#     }
# resC = testC.favGenres(userSongs, songGenres)
# print(resC)
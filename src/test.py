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

        temp = list(connections)
        res = []
        for item in temp:
            tempres = []
            for i in range(len(item)):
                tempres.append(item[i])
            res.append(tuple(tempres))
        return res


# test=Critical_connection()
# res = test.find(5, [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]])
# print(res)
test=Solution()
#res=test.criticalConnections(5, [[0, 1], [0, 2], [2, 3], [0, 3], [3, 4]])
res = test.criticalConnections(5, [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]])
print(res)
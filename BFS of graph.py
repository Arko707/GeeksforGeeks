
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        bfs = []
        k = [0]
        while len(k) != 0:
            if k[0] not in bfs:
                bfs.append(k[0])
                for V in adj[k[0]]:
                    if V not in bfs:
                        k.append(V)
            k.pop(0)
        return bfs
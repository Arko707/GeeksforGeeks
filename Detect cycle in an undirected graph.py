
class Solution: 
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V, adj):
        visited=[False for i in range(V)]
        def cycle(s,parent):
            visited[s]=True
            for n in adj[s]:
                if not visited[n]:
                    if cycle(n,s):
                        return 1
                elif n!=parent:
                    return 1
            return 0
        def detect():
            for n in range(V):
                if visited[n]==False:
                    if cycle(n,-1):
                        return True
            return False
        return detect()
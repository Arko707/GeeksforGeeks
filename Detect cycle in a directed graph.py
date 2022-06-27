
class Solution:
    def dfs(visited,recstack,adj,v):
        visited[v]=True
        recstack[v]=True
        for n in adj[v]:
            if visited[n]==False:
                if Solution.dfs(visited,recstack,adj,n):
                    return True
            elif recstack[n]==True:
                return True
        recstack[v]=False
        return False
       
    def isCyclic(self, V, adj):
        visited=[False]*(V+1)
        recstack=[False]*(V+1)
        for n in range(V):
            if visited[n]==False:
                if Solution.dfs(visited,recstack,adj,n):
                    return True
        return False
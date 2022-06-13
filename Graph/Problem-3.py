
class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def DFS(self,node,adj,visited,ans):
        ans.append(node)
        visited[node]=True
        for adjacentNode in adj[node]:
            if(visited[adjacentNode]== False):
                self.DFS(adjacentNode,adj,visited,ans)
                
    def dfsOfGraph(self, V, adj):
            ans=[]
            visited=[False for i in range(V)]
            self.DFS(0,adj,visited,ans)
            return ans
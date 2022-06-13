class Solution:
    
    #Function to detect cycle in a directed graph.
    def CheckCycleInDirectedUsingDFS(self,node,adj,visited,dfsVisited):
        visited[node]=True
        dfsVisited[node]=True
        
        for adjacentNode in adj[node]:
            if(visited[adjacentNode]== False):
                if(self.CheckCycleInDirectedUsingDFS(adjacentNode,adj,visited,dfsVisited)):
                    return True
            elif(dfsVisited[adjacentNode]==True):
                return True
                
        dfsVisited[node]=False
        return False   
        
    def isCyclic(self, V, adj):
        visited=[False for i in range(V)]
        dfsVisited=[False for i in range(V)]
            
        for i in range(V):
            if(visited[i]==False):
                if(self.CheckCycleInDirectedUsingDFS(i,adj,visited,dfsVisited)):
                    return 1
        return 0
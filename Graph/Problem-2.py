#Implement BFS Algorithm

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def BFS(self,start,visited,ans,adj):
        queue=[]
        queue.append(start)
        visited[start]=True
        
        while(queue):
            node=queue[0]
            queue.pop(0)
            ans.append(node)
            for adjacentNode in adj[node]:
                if(visited[adjacentNode]==False):
                    queue.append(adjacentNode)
                    visited[adjacentNode]=True
            
    def bfsOfGraph(self, V, adj):
        ans=[]
        visited=[False for i in range(V)]
        self.BFS(0,visited,ans,adj)
        return ans
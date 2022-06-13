# Detect Cycle in Undirected Graph 

class Solution:
    
    #Function to detect cycle in an undirected graph.
    def CheckCycleUsingBFS(self,start,visited,adj):
        queue=[]
        queue.append([start,-1])
        visited[start]=True

        while(queue):
            nodeData=queue[0]
            node=nodeData[0]
            parent=nodeData[1]
            queue.pop(0)
            for adjacentNode in adj[node]:
                if(visited[adjacentNode]==False):
                    queue.append([adjacentNode,node])
                    visited[adjacentNode]=True
                elif(adjacentNode!=parent):
                    return True
        return False
        
        
    def isCycle(self, V, adj):
        visited=[False for i in range(V)]
        for i in range(V):
            if(visited[i]==False):
                if(self.CheckCycleUsingBFS(i,visited,adj)):
                    return 1
        return 0
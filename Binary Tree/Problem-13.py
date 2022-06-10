# https://practice.geeksforgeeks.org/problems/zigzag-tree-traversal/1#

#Zig-Zag Traversal 



#Solution Using Level Order Traversal and flag

def zigZagTraversal(self, root):  
    queue=[]
    ans=[]
    
    leftToRight=True
    
    queue.append(root)
    
    while(queue):

        size=len(queue)
        tempList=[-1]*size
        for i in range(size):
            cur=queue[0]
            queue.pop(0)
            index= i if leftToRight else size-1-i
            tempList[index]=cur.data
            if(cur.left):
                queue.append(cur.left)
            if(cur.right):
                queue.append(cur.right)
        ans=ans+tempList
        leftToRight= False if leftToRight else True
                
    return ans
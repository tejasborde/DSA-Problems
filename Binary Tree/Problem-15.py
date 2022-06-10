
# https://practice.geeksforgeeks.org/problems/diagonal-traversal-of-binary-tree/1/

#Diagonal Traversal of Binary Tree
def diagonal(root):
    
    queue=[]
    queue.append(root)
    ans=[]
    
    while(queue):
        node=queue.pop(0)  
        while(node):
            ans.append(node.data)
            if(node.left):
                queue.append(node.left)
            node=node.right
    return ans
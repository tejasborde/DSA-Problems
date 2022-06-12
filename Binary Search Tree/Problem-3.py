# Min value BST 

def minValue(root):
    if(root==None):
        return -1 
    minNode=root.data
    while(root):
        minNode=min(minNode,root.data)
        root=root.left
    return minNode
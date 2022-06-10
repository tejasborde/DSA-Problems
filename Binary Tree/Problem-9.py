# https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1#

#Get the Left View of Binary Tree


# def height(root):
#     if(root):
#         return 1+max(height(root.left),height(root.right))
#     return 0
    
# def getLeftView(root,ans,level):
#     if(root):
#         if(ans[level]==False):
#             ans[level]=root.data
#         getLeftView(root.left,ans,level+1)
#         getLeftView(root.right,ans,level+1)
    
# def LeftView(root):
#     heightOfTree=height(root)
#     ans=[False for i in range(heightOfTree)]
#     getLeftView(root,ans,0)
#     return ans


#============================================================

# Iterative Apporach
from collections import deque
def leftView(root):  
    if root is None:
        return

    q = deque()
    q.append(root)
    while q:    
        # Get number of nodes for each level
        n = len(q)
        # Traverse all the nodes of the
        # current level
        for i in range(1,n+1):
            
            # Get the front node in the queue
            node = q.popleft()
            # Print the last node of each level
            if(i==1):
                print(node.data, end = " ")
            # If left child is not null push it
            # into the queue
            if node.left:
                q.append(node.left)
            # If right child is not null push
            # it into the queue
            if node.right:
                q.append(node.right)
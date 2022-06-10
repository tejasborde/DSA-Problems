#Right View of Binary Tree


# def getrightView(self,root,level,max_level,ans):
#     if root is None:
#         return
#     if (max_level[0] < level):
#         ans.append(root.data)
#         max_level[0] = level
#     self.getrightView(root.right, level+1, max_level,ans)
#     self.getrightView(root.left, level+1, max_level,ans)
        
# def rightView(self,root):
#     ans=[]
#     self.getrightView(root,1,[0],ans)
#     return ans



#==========================================

# Iterative Apporach
from collections import deque
def rightView(root):  
    if root is None:
        return

    q = deque()
    q.append(root)
    while q:    
        # Get number of nodes for each level
        n = len(q)
        # Traverse all the nodes of the
        # current level
        while n > 0:
            n -= 1   
            # Get the front node in the queue
            node = q.popleft()
            # Print the last node of each level
            if n == 0:
                print(node.data, end = " ")
            # If left child is not null push it
            # into the queue
            if node.left:
                q.append(node.left)
            # If right child is not null push
            # it into the queue
            if node.right:
                q.append(node.right)

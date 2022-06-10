import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


# https://practice.geeksforgeeks.org/problems/level-order-traversal/1#

#Level Order Traversal of Binary Tree
# Input:
#     1
#   /   \ 
#  3     2
# Output:1 3 2

# Input:
#         10
#      /      \
#     20       30
#   /   \
#  40   60
# Output:10 20 30 40 60


def levelOrder(self,root ):
    visited=[]
    queue=[]
    queue.append(root)
    visited.append(root.data)
    
    while(len(queue)!=0):
        node=queue.pop(0)
        
        if(node.left!=None):
            queue.append(node.left)
            visited.append(node.left.data)
        if(node.right!=None):
            queue.append(node.right)
            visited.append(node.right.data)
    
    return visited
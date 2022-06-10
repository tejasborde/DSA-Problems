import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')

#Reverse Level Order traversal of Binary tree

# Input :
#        10
#       /  \
#      20   30
#     / \ 
#    40  60

# Output: 40 60 20 30 10
# Explanation:
# Traversing level 2 : 40 60
# Traversing level 1 : 20 30
# Traversing level 0 : 10

#Using Recusrion
# def postOrder(root,ans):
#     if(root!=None):
#         postOrder(root.left,ans)
#         postOrder(root.right,ans)
#         ans.append(root.data)
#     return ans


#Using Double Ended Queue
#Same as level order traversal just append left node to queue first and 
#node to the left of ans array

from collections import deque
def reverseLevelOrder(root):
    q = deque()
    q.append(root)
    ans = deque()
    while q:
        node = q.popleft()
        if node is None:
            continue
        
        ans.appendleft(node.data)
        
        if node.right:
            q.append(node.right)
            
        if node.left:
            q.append(node.left)
            
    return ans
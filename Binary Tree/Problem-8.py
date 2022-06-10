#Postorder traversal of B Tree
# https://practice.geeksforgeeks.org/problems/postorder-traversal/1

#Recursive Solution
# def postOrderTraversal(root):
#     if(root):
#         postOrderTraversal(root.left)
#         postOrderTraversal(root.right)
#         print(root.data)


#=======================================================================

#iterative Solution 

from collections import deque       
def postOrder(root):
    stack=[]
    output=deque()
    
    stack.append(root)
    
    while(stack):
        
        node=stack.pop()
        output.appendleft(node.data)
        
        if(node.left):
            stack.append(node.left)
        if(node.right):
            stack.append(node.right)
    
    return output
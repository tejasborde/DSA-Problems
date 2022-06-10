# https://practice.geeksforgeeks.org/problems/preorder-traversal/1#

#Preorder Traversal of Binary Tree

#Recursive Solution 

# def preOrderTraversal(root):
#     if(root):
#         print(root.data)
#         preOrderTraversal(root.left)
#         preOrderTraversal(root.right)


#=======================================================================

#Iterative Solution
def preorder(root):
    ans=[]
    stack=[]
    
    while(len(stack)!=0 or root!=None):
        if(root!=None):
            ans.append(root.data)
            stack.append(root)
            root=root.left
        else:
            root=stack.pop()
            root=root.right
    return ans
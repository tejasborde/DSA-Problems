# https://practice.geeksforgeeks.org/problems/inorder-traversal/1#


#Inorder Traversal of Tree


#Recusive Solution
# def inOrderTraversal(self,root):
#     if(root):
#         self.inOrderTraversal(root.left)
#         print(root.data)
#         self.inOrderTraversal(root.right)

#==============================================================================

#Iterative Solution Using stack
#Push till not none and move to left
#Pop and print data and move to right till stack is not empty or root is not none

def InOrder(self,root):
    ans=[]
    stack=[]
    while(len(stack)!=0 or root!=None):
        if(root!=None):
            stack.append(root)
            root=root.left
        else:
            root=stack.pop()
            ans.append(root.data)
            root=root.right
    return ans
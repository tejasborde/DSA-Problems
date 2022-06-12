# Build Binary Search Tree from PreOrder

#If the element is less than the root then pass it to left with upper bound=root.val
#else pass it to right with upper bound=previous upper bound

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self,preorder,index,upperBound):
        if(index[0]==len(preorder) or preorder[index[0]]>upperBound):
            return None
        root=Node(preorder[index[0]])
        index[0]+=1
        root.left=self.buildTree(preorder,index,root.val)
        root.right=self.buildTree(preorder,index,upperBound)
        return root
    
    def bstFromPreorder(self, preorder) :
        index=[0]
        return self.buildTree(preorder,index,float('inf'))
#PreOrder to PostOrder


#Given array of preOrder

#Solution 1
#create BST using the preorder array using upperBound Concept
#traverse the tree using postorder traversal to get the output
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


def buildTree(preorder,index,upperBound):
        if(index[0]==len(preorder) or preorder[index[0]]>upperBound):
            return None
        root=Node(preorder[index[0]])
        index[0]+=1
        root.left=buildTree(preorder,index,root.data)
        root.right=buildTree(preorder,index,upperBound)
        return root
    
    
def post_order(pre, size):
    index=[0]
    root=buildTree(pre,index,float('inf'))
    return root
#Convert Binary Tree to BST without changing the structure of Tree
# https://practice.geeksforgeeks.org/problems/binary-tree-to-bst/1#


def inOrderOfTree(self,root,ans):
        if(root):
            self.inOrderOfTree(root.left,ans)
            ans.append(root.data)
            self.inOrderOfTree(root.right,ans)
            
def inOrderOfBST(self,root,inorder,index):
    if(root):
        self.inOrderOfBST(root.left,inorder,index)
        root.data=inorder[index[0]]
        index[0]+=1
        self.inOrderOfBST(root.right,inorder,index)
        
def binaryTreeToBST(self, root):
    ans=[]
    self.inOrderOfTree(root,ans)
    ans.sort()
    index=[0]
    self.inOrderOfBST(root,ans,index)
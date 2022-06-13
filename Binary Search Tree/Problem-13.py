# https://practice.geeksforgeeks.org/problems/find-k-th-smallest-element-in-bst/1#

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    # Return the Kth smallest element in the given BST 
    def inOrderOfTree(self,root,ans):
        if(root):
            self.inOrderOfTree(root.left,ans)
            ans.append(root.data)
            self.inOrderOfTree(root.right,ans)
            
    def KthSmallestElement(self, root, K): 
        ans=[]
        self.inOrderOfTree(root,ans)
        if(len(ans)<K):
            return -1
        return ans[K-1]
# https://practice.geeksforgeeks.org/problems/kth-largest-element-in-bst/1

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def inOrderOfTree(self,root,ans):
        if(root):
            self.inOrderOfTree(root.left,ans)
            ans.append(root.data)
            self.inOrderOfTree(root.right,ans)
    def kthLargest(self,root, k):
        ans=[]
        self.inOrderOfTree(root,ans)
        
        return ans[-k]
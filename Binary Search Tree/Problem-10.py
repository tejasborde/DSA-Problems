#Convert Normal BST to  BALANCED BST
# https://practice.geeksforgeeks.org/problems/normal-bst-to-balanced-bst/1/


class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


class Solution:
    def inOrderOfTree(self,root,ans):
        if(root):
            self.inOrderOfTree(root.left,ans)
            ans.append(root.data)
            self.inOrderOfTree(root.right,ans)
    
    def bulidBSTfromArray(self,nums):
        if(not nums):
            return None
        mid=(len(nums)//2)
	    
        root=Node(nums[mid])
        root.left=self.bulidBSTfromArray(nums[:mid])
        root.right=self.bulidBSTfromArray(nums[mid+1:])
        return root
	    
            
    def buildBalancedTree(self,root):
        ans=[]
        self.inOrderOfTree(root,ans)
        root=self.bulidBSTfromArray(ans)
        return root
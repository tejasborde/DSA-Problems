# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/
#Sorted Array to BST

class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

        
class Solution:
    def bulidBSTfromArray(self,nums):
            if(not nums):
                return None
            mid=(len(nums)//2)
            
            root=Node(nums[mid])
            root.left=self.bulidBSTfromArray(nums[:mid])
            root.right=self.bulidBSTfromArray(nums[mid+1:])
            return root
        
    def preOrder(self,root,ans):
        if(root):
            ans.append(root.data)
            self.preOrder(root.left,ans)
            self.preOrder(root.right,ans)
        
    def sortedArrayToBST(self, nums):
        root=self.bulidBSTfromArray(nums)
        preOrderTravseral=[]
        self.preOrder(root,preOrderTravseral)
        
        return preOrderTravseral
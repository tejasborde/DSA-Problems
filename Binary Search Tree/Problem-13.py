#https://practice.geeksforgeeks.org/problems/brothers-from-different-root/1


#Count Pairs with Sum K from Two BST
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def find(self,root,value):
        if(root):
            if(root.data==value):
                return True
            x=False
            y=False
            
            if(root.data<value):
                x=self.find(root.right,value)
            elif(root.data>value):
                y=self.find(root.left,value)
            return x or y
        return False
    
    def inOrderTree(self,root1,root2,count,x):
        if(root1):
            self.inOrderTree(root1.left,root2,count,x)
            if(self.find(root2,x-root1.data)):
                count[0]+=1
            self.inOrderTree(root1.right,root2,count,x)
    
    def countPairs(self, root1, root2, x): 
        
        count=[0]
        self.inOrderTree(root1,root2,count,x)
        
        return count[0]
        
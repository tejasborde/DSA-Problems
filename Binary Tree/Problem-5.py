
# https://practice.geeksforgeeks.org/problems/mirror-tree/1
#Mirror of Tree

def mirror(self,root):
    if(root==None):
        return 
    self.mirror(root.left)
    self.mirror(root.right)
    
    root.left,root.right=root.right,root.left
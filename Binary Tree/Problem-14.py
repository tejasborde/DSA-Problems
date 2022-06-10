# https://practice.geeksforgeeks.org/problems/check-for-balanced-tree/1#

#Check if Tree is Balanced or Not 

def checkForBalanched(self,root):
    if(root):
        lh=self.checkForBalanched(root.left)
        rh=self.checkForBalanched(root.right)
        if(lh==-1 or rh==-1 or abs(lh-rh)>1):
            return -1
        return 1+max(lh,rh)
    return 0
        
def isBalanced(self,root):
    return 0 if self.checkForBalanched(root)==-1 else -1
# https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1#
#Diameter of Binary tree



#Solution 1 : Bruteforce O(n^2)

# diameter of tree=max(lHeight+rheight,max(ldiameter,rdiameter))
# def diameter(root):
 
#     if root is None:
#         return 0
#     lheight = height(root.left)
#     rheight = height(root.right)

#     ldiameter = diameter(root.left)
#     rdiameter = diameter(root.right)
#     return max(lheight + rheight, max(ldiameter, rdiameter))



#Solution 2 : Using Height of Tree Function O(n)
# def calDiameterwithHeight(self,root,maxDiameter):
#     maxDiameter
#     if(root==None):
#         return 0
    
#     lh=self.calDiameterwithHeight(root.left,maxDiameter)
#     rh=self.calDiameterwithHeight(root.right,maxDiameter)
    
#     maxDiameter[0]=max(maxDiameter[0],lh+rh+1)
    
#     return 1+max(lh,rh)
    
# def diameter(self,root):
#     maxDiameter=[0]
#     self.calDiameterwithHeight(root,maxDiameter)
#     return maxDiameter[0]
#Flatten Binary Tree into Link List wihtout using extra space

def flatten(self, root):
    if(root==None or root.left==None and root.right==None ):
        return
    if(root.left):
        self.flatten(root.left)
        
        temp=root.right
        root.right=root.left
        root.left=None
        
        tail=root.right
        
        while(tail.right):
            tail=tail.right
        
        tail.right=temp
        
    self.flatten(root.right)
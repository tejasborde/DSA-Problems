#Delete Node From BST

def deleteNodeFromBST(root,X):
    
    parent=None
    temp=root
    
    while(temp!=None and temp.data!=X):
        parent=temp
        if(X<temp.data):
            temp=temp.left
        else:
            temp=temp.right
    
    if(temp==None):
        return root
    else:
        #If the node to be deleted is leaf node
        if(temp.left==None and temp.right==None):
            if(root==temp):
                return None
            elif(parent.left==temp):
                parent.left=None
            else:
                parent.right=None
        #If the node to be deleted has left child node
        elif(temp.left!=None and temp.right==None):
            if(parent.left==temp):
                parent.left=temp.left
            else:
                parent.right=temp.left
        #If the node to be deleted has right child node
        elif(temp.left==None and temp.right!=None):
            if(parent.left==temp):
                parent.left=temp.right
            else:
                parent.right=temp.right
        #If the node to be deleted has left and right child       
        elif(temp.left!=None and temp.right!=None):
            nextGreater=temp.right
            
            while(nextGreater.left):
                nextGreater=nextGreater.left
            
            val=nextGreater.data
            
            deleteNodeFromBST(root,val)   
            temp.data=val
        
        return root
            
            

#Function to delete a node from BST.
def deleteNode(root, X):
    ans=deleteNodeFromBST(root,X)
    return ans
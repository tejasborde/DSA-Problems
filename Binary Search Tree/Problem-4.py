#Find Inorder predecessor and succesor

def inOrderSucc(root,key):
    ans=None
    while(root):
        if(root.key<=key):
            root=root.right
        else:
            ans=root
            root=root.left
    return ans

def inOrderPre(root,key):
    ans=None
    
    while(root):
        if(root.key>=key):
            root=root.left
        else:
            ans=root
            root=root.right
    return ans
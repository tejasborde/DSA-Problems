#check if BST has dead ends

def checkDeads(node, mini, maxi):
     
    if node is None:
        return False

    if abs(mini-maxi)==0:
        return True
    
    return checkDeads(node.left, mini, node.data-1) or checkDeads(node.right, node.data+1, maxi)

def isdeadEnd(root):
    return 1 if checkDeads(root, 1, float('inf')) else 0
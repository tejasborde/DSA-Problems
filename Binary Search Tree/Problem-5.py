#Check for BST

def isBSTUtil(self,node, mini, maxi):
     
    if node is None:
        return True

    if node.data < mini or node.data > maxi:
        return False
    
    return self.isBSTUtil(node.left, mini, node.data -1) and self.isBSTUtil(node.right, node.data+1, maxi)
            
def isBST(self, root):
    return self.isBSTUtil(root, float('-inf'), float('inf'))
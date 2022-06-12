#Search Node in BST


def search(self, node, x):
    ans=0
    
    stack=[]
    
    while(len(stack)!=0 or node):
        if(node):
            stack.append(node)
            node=node.left
        else:
            node=stack.pop()
            if(node.data==x):
                return 1
            node=node.right
    return 0
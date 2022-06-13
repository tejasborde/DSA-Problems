#Count Node of BST that lie in given Range


def countNodes(root,count,l,h):
    if(root):
        countNodes(root.left,count,l,h)
        if(root.data>=l and root.data<=h):
            count[0]+=1
        countNodes(root.right,count,l,h)


def getCountofNodes(root,l,h):
    count=[0]
    countNodes(root, count, l, h)
    return count[0]

#bottom view of binary tree
#print last node of each vertical line

def bottomView(self, root):
    if(root == None):
        return
    q = []
    m = dict()
    hd = 0
    root.hd = hd

    q.append(root)
    
    while(len(q)):
        root = q[0]
        hd = root.hd

        m[hd]=root.data
        if(root.left):
            root.left.hd = hd - 1
            q.append(root.left)
    
        if(root.right):
            root.right.hd = hd + 1
            q.append(root.right)
    
        q.pop(0)
    
    printList=[]
    for i in sorted(m):
        printList.append(m[i])
    
    return printList
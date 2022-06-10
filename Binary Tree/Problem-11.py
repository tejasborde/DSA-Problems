# https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1#

#Print Top View of Binary Tree


#print 1st node of each vertical line

def topView(self,root):
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
        if hd not in m:
            m[hd] = root.data
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
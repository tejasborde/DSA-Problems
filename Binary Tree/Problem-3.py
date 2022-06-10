import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')



#Height of Binary Tree
# def height(self, root):
#     if root!=None:
        
#         leftHeight=self.height(root.left) 
#         rightHeight=self.height(root.right) 
        
#         return max(leftHeight,rightHeight)+1
#     return 0


#Height of Tree Using BFS
def height(self, root):
    queue=[]
    queue.append(root)
    queue.append(None)
    h=0
    
    while(len(queue)!=0):
        node=queue.pop(0)

        if(node==None):
            h+=1
        if(node!=None):
            if(node.left!=None):
                queue.append(node.left)
    
            if(node.right!=None):
                queue.append(node.right)
        elif(len(queue)>0):
            queue.append(None)
    
    return h
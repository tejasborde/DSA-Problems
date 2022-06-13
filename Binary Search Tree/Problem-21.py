import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')

class nodeData:
    def __init__(self,largest,smallest,size):
        self.largest=largest
        self.smallest=smallest
        self.size=size

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right
        
class Solution:
    # Return the size of the largest sub-tree which is also a BST
    def sizeOfLargestBST(self,root):
        if(root):
            left=self.sizeOfLargestBST(root.left)
            right=self.sizeOfLargestBST(root.right)
            if(left.largest<root.data and right.smallest>root.data):
                largest=max(right.largest,root.data)
                smallest=min(root.data,left.smallest)
                size=1+left.size+right.size 
                newData=nodeData(largest,smallest,size)
                return newData
            else:
                size=max(left.size,right.size )
                largest=float('inf')
                smallest=float('-inf')
                newData=nodeData(largest,smallest,size)
                return newData
        newData=nodeData(float('-inf'),float('inf'),0)
        return newData
            
    def largestBst(self, root):
        data=self.sizeOfLargestBST(root)
        return data.size


def printInorder(root):
    if(root):
        printInorder(root.left)
        print(root.data,end=" ")
        printInorder(root.right)

root=Node(1)
root.left=Node(4)
root.right=Node(4)
root.left.left=Node(6)
root.left.right=Node(8)

# printInorder(root)

S=Solution()
ans=S.largestBst(root)
print(ans)
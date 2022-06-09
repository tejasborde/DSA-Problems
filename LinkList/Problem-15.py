import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


#Find the middle of the linkList
def findMid(self, head):
    if(head==None or head.next==None):
        return head.data
    slow=head
    fast=head

    while(fast!=None and fast.next!=None):
        slow=slow.next 
        fast=fast.next.next
    return slow.data
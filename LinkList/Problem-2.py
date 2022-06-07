import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')



# Reverse a linked list By Groups of Size K
# Input:
# LinkedList: 1->2->2->4->5->6->7->8
# K = 4
# Output: 4 2 2 1 8 7 6 5 
# Explanation: 
# The first 4 elements 1,2,2,4 are reversed first 
# and then the next 4 elements 5,6,7,8. Hence, the 
# resultant linked list is 4->2->2->1->8->7->6->5.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
 
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next
        print()

    def reverseBygroupsOfSizeK(self,head,k):
        if(head==None):
            return head
        cur=head
        next=None
        prev=None
        count=0
        while(cur is not None and count < k):
            next=cur.next 
            cur.next=prev
            prev=cur 
            cur=next
            count+=1
        
        if(next!=None):
            head.next=self.reverseBygroupsOfSizeK(next, k)
        return prev
    
        
    
l=LinkedList()

l.push(8)
l.push(7)
l.push(6)
l.push(5)
l.push(4)
l.push(2)
l.push(2)
l.push(1)

l.printList()

k=4
l.head=l.reverseBygroupsOfSizeK(l.head, k)

l.printList()

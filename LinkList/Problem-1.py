import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')



# Reverse a linked list
# Input: Head of following linked list 
# 1->2->3->4->NULL 

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

    def reverse(self):
        prev=None
        cur=self.head 
        next=cur.next 

        while(cur is not None):
            next=cur.next
            cur.next=prev
            prev=cur 
            cur=next
        
        self.head=prev

    def reverseRecusive(self,head):
        if (head is None  or head.next is None):
            return head 
        remainingList=self.reverseRecusive(head.next)

        head.next.next=head 
        head.next=None

        return remainingList

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
l.head=l.reverseRecusive(l.head)
l.printList()

import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')


#Remove Duplicate Nodes from UN-Sorted LinkList


class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
        self.flag=False
class LinkList:
    def __init__(self):
        self.head = None
    
    def insertNodeatEnd(self,data):
        if(self.head==None):
            self.head=Node(data)
            return self.head
        else:
            cur=self.head
            while(cur.next!=None):
                cur=cur.next 
            cur.next=Node(data)
            return self.head
    

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

    #Make use of set to store previous elements
    def removeDuplicates(self,head):
        if head is None or head.next is None:
            return head
        s=set()
        cur=head
        s.add(cur.data)
        while(cur.next!=None):
            if(cur.next.data in s):
                cur.next=cur.next.next 
            else:
                cur=cur.next
                s.add(head.data)
        



llist = LinkList()
llist.insertNodeatEnd(5)
llist.insertNodeatEnd(2)
llist.insertNodeatEnd(2)
llist.insertNodeatEnd(4)


llist.printList()

llist.removeDuplicates(llist.head)

llist.printList()
import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')


#Remove Duplicate Nodes from Sorted LinkList


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

    def removeDuplicates(self,head):

        temp=head 

        while(temp.next!=None):
            if(temp.data==temp.next.data):
                temp.next=temp.next.next
            else:
                temp=temp.next
        
# 90 93 95 96 98  98  98

llist = LinkList()
llist.insertNodeatEnd(90)
llist.insertNodeatEnd(93)
llist.insertNodeatEnd(95)
llist.insertNodeatEnd(96)
llist.insertNodeatEnd(98)
llist.insertNodeatEnd(98)
llist.insertNodeatEnd(98)



llist.printList()

llist.removeDuplicates(llist.head)

llist.printList()

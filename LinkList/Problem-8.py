import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')

# Move last element to front of a given Linked List
# INPUT : 1->2->3->4->5
#OUTPUT : 5->1->2->3->4


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


    def moveLastNodetoFirst(self,head):
        first=head
        prev=head
        next=prev.next

        while(next.next!=None):
            prev=next
            next=next.next 
        
        next.next=first
        prev.next=None
        return next
       




llist = LinkList()
llist.insertNodeatEnd(1)
llist.insertNodeatEnd(2)
llist.insertNodeatEnd(3)
llist.insertNodeatEnd(4)
llist.insertNodeatEnd(5)

llist.printList()


llist.head=llist.moveLastNodetoFirst(llist.head)

llist.printList()
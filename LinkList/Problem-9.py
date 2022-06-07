import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')



#Add 1 to the Number Repeseneted by the nodes of Link List
# Example 1:

# Input:
# LinkedList: 4->5->6
# Output: 457 
# Example 2:

# Input:
# LinkedList: 1->2->3
# Output: 124 

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

    def reverse(self,head):

        cur=head
        prev=None
        next=cur.next

        while(cur!=None):
            next=cur.next
            cur.next=prev
            prev=cur 
            cur=next 
        self.head=prev
        return self.head

    def addOne(self,head):
        head=self.reverse(head)
        cur=head
        carry=True
        while(cur!=None and carry==True):
            if(cur.data==9 and cur.next==None):
                cur.data=1
                newNode=Node(0)
                newNode.next=head
                head=newNode
            elif(cur.data==9):
                cur.data=0
            else:
                cur.data+=1
                carry=False

            cur=cur.next
        head=self.reverse(head)
        return head




llist = LinkList()
llist.insertNodeatEnd(9)
llist.insertNodeatEnd(9)
llist.insertNodeatEnd(9)


llist.printList()

llist.addOne(llist.head)

llist.printList()
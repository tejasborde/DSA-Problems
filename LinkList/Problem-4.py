import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')



#remove loop from linkkist


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
    
    def detectLoop(self):
        slow=self.head
        fast=self.head

        while(slow!=None and fast!=None):
            slow=slow.next 
            fast=fast.next.next
            if(slow==fast):
                return True 
        return False

    
    def removeLoop(self):
        slow=self.head
        fast=self.head

        while(slow!=None and fast!=None and fast.next!=None):
            slow=slow.next 
            fast=fast.next.next
            if(slow==fast):
                break 

        cur=self.head 
        temp=slow 

        while(cur.next!=temp.next):
            cur=cur.next 
            temp=temp.next 
        print("Loop was present from "+str(temp.data)+" -> ",str(temp.next.data))
        temp.next=None 
        
        print("Loop Removed")
        return self.head  


llist = LinkList()
llist.insertNodeatEnd(20)
llist.insertNodeatEnd(4)
llist.insertNodeatEnd(15)
llist.insertNodeatEnd(10)
llist.insertNodeatEnd(3)
llist.insertNodeatEnd(9)
llist.insertNodeatEnd(11)
# 20->4->15->->10->3->9->11

# Create a loop for testing
ThreeNode=llist.head.next.next
LoopNode=llist.head.next.next.next.next.next.next
LoopNode.next=ThreeNode

if llist.detectLoop():
    print("Loop Found")
    llist.removeLoop()
    llist.printList()
else:
    print("Loop Not Found")
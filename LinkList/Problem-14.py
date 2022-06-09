import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')

#QuickSort LinkList

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


class LinkList:
    # def __init__(self):
    #     self.head = None
    
    def insertNodeatEnd(self,head,data):
        if(head==None):
            head=Node(data)
            return head
        else:
            cur=head
            while(cur.next!=None):
                cur=cur.next 
            cur.next=Node(data)
            return head
    

def printList(head):
    temp = head
    while(temp):
        print(temp.data, end=" ")
        temp = temp.next
    print()





def partition(start,end):
    if(start==end or start==None or end==None):
        return start
    head=start
    pivot=end.data
    cur=start
    previousofPivot=start

    while(start!=end):
        if(start.data<pivot):
            previousofPivot=cur
            temp=cur.data
            cur.data=start.data 
            start.data=temp 
            cur=cur.next
        start=start.next 
    

    #swap the cur node data and pivot node data
    temp=cur.data
    cur.data=pivot
    end.data=temp 
    
    #return one node previous to pivot
    return previousofPivot

def quickSort(start,end):
    if(start==None or start==end or start==end.next):
        return None 
    
    pivotPrevious=partition(start, end)
    quickSort(start, pivotPrevious)


    #if pivot is moved to start
    if(pivotPrevious!=None and pivotPrevious==start):
        quickSort(pivotPrevious.next, end)

    #if pivot is in between the list
    if(pivotPrevious!=None and pivotPrevious.next!=None):
        quickSort(pivotPrevious.next.next, end)

    return start
    
l=LinkList()
head=Node(15)
l.insertNodeatEnd(head,10)
l.insertNodeatEnd(head,5)
l.insertNodeatEnd(head,20)
l.insertNodeatEnd(head,3)
l.insertNodeatEnd(head,2)




printList(head)
end=head
while (end.next != None):
    end = end.next
head=quickSort(head, end)
printList(head)
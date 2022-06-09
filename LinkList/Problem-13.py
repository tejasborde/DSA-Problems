import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


#LinkList Merge Sort


class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


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




def getMiddleOfList(head):
    if(head==None or head.next==None):
        return head
    slow=head
    fast=slow.next

    while(fast!=None and fast.next!=None):
        slow=slow.next 
        fast=fast.next.next
    return slow


def mergeSort(listHead):
    if listHead == None or listHead.next == None:
        return listHead
    low=listHead
    mid=getMiddleOfList(listHead)
    midPlusOne=mid.next
    mid.next=None

    left=mergeSort(low)
    right=mergeSort(midPlusOne)
    listHead=mergeBothList(left,right)

    return listHead

def mergeBothList(low,midPlusOne):
    answer=Node(-1)
    temp=answer
    while(low!=None and midPlusOne!=None):
        if(low.data<=midPlusOne.data):
            temp.next=low 
            low=low.next 
            temp=temp.next 
        else:
            temp.next=midPlusOne
            midPlusOne=midPlusOne.next
            temp=temp.next 
    
    if(low!=None):
        while(low!=None):
            temp.next=low 
            low=low.next 
            temp=temp.next 
    else:
        while(midPlusOne!=None):
            temp.next=midPlusOne
            midPlusOne=midPlusOne.next
            temp=temp.next  

    return answer.next

    
l=LinkList()

l.insertNodeatEnd(15)
l.insertNodeatEnd(10)
l.insertNodeatEnd(5)
l.insertNodeatEnd(20)
l.insertNodeatEnd(3)
l.insertNodeatEnd(2)




l.printList()

l.head=mergeSort(l.head)

l.printList()

# low,mid=getMiddleOfList(l.head)
# midPlusOne=mid.next
# mid.next=None
# print(low.data,mid.data)

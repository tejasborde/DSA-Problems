import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')

#Intersection point of two sorted list

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

def getInterSectionNode(l1,l2):
    if(l1==None or l2==None):
        return -1
    
    cur1=l1 
    cur2=l2 

    while(cur1!=None and cur2!=None):
        if(cur1==cur2):
            return cur1.data 
        cur1=cur1.next 
        cur2=cur2.next

    return -1

def IntersectionPointOfTwoLists(l1,l2):
    if(l1==None or l2==None):
        return -1
    
    count1=0
    count2=0

    list1=l1
    while(list1):
        count1+=1
        list1=list1.next 
    list2=l2
    while(list2):
        count2+=1
        list2=list2.next 
    
    d=abs(count1-count2)
    if(count1>count2):
        for i in range(d):
            l1=l1.next
        return getInterSectionNode(l1,l2)
    else:
        for i in range(d):
            l2=l2.next
        return getInterSectionNode(l1,l2)
    


first = LinkList()

# first.insertNodeatEnd(4)
# first.insertNodeatEnd(1)
# first.insertNodeatEnd(8)
# first.insertNodeatEnd(4)
# first.insertNodeatEnd(5)




second = LinkList()
# second.insertNodeatEnd(5)
# second.insertNodeatEnd(6)
# second.insertNodeatEnd(1)
# first.insertNodeatEnd(8)
# first.insertNodeatEnd(4)
# first.insertNodeatEnd(5)


print(IntersectionPointOfTwoLists(first.head, second.head))
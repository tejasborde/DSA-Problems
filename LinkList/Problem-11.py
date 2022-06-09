import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


#Intersection of Two Sorted Link List
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




#Solution 1 Using Set

# def interSectionOftwoLists(first,second):
#     if(first==None or second==None):
#         return None 

#     s=set()
#     added=set()
#     while(first!=None):
#         s.add(first.data)
#         first=first.next
    
#     head=Node(-1)
#     temp=head
#     while(second!=None):
#         if(second.data in s and second.data not in added):
#             newNode=Node(second.data)
#             temp.next=newNode
#             temp=temp.next 
#             added.add(second.data)
#         second=second.next

#     return head.next 

def interSectionOftwoLists(f,s):
    if(f==None or s==None):
        return None 

    head=Node(-1)
    temp=head

    while(f!=None and s!=None):
        if(f.data==s.data):
            newNode=Node(f.data)
            temp.next=newNode
            temp=temp.next
            f=f.next 
            second=s.next 
        elif(f.data < s.data):
            f=f.next 
        else:
            s=s.next
    
    return head.next


first = LinkList()
first.insertNodeatEnd(1)
first.insertNodeatEnd(3)
first.insertNodeatEnd(7)
first.insertNodeatEnd(8)
first.insertNodeatEnd(9)



second = LinkList()
second.insertNodeatEnd(3)
second.insertNodeatEnd(5)
second.insertNodeatEnd(9)
second.insertNodeatEnd(9)


newList=LinkList()
newList.head=interSectionOftwoLists(first.head,second.head)

newList.printList()
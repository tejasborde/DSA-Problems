import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


# Add two numbers represented by linked lists
# Input:
# N = 2
# valueN[] = {4,5}
# M = 3
# valueM[] = {3,4,5}
# Output: 3 9 0  
# Explanation: For the given two linked
# list (4 5) and (3 4 5), after adding
# the two linked list resultant linked
# list will be (3 9 0).


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
        return prev

    def addNumbers(self,first,second):
        first=self.reverse(first)
        second=self.reverse(second)
        head=Node(0)
        carry=0
        temp=head
        while(first!=None and second!=None):
            s=first.data+second.data+carry
            carry=0
            if(s>9):
                carry=s//10
                data=s%10
                temp.next=Node(data)
            else:
                temp.next=Node(s)
            
            temp=temp.next 
            first=first.next
            second=second.next
        
        if(first==None):
            while(second!=None):
                s=second.data+carry
                carry=0
                if(s>9):
                    carry=s//10
                    data=s%10
                    temp.next=Node(data)
                else:
                    temp.next=Node(s)
                second=second.next 
                temp=temp.next
        else:
             while(first!=None):
                s=first.data+carry
                carry=0
                if(s>9):
                    carry=s//10
                    data=s%10
                    temp.next=Node(data)
                else:
                    temp.next=Node(s)
                first=first.next 
                temp=temp.next
        if(carry==1):
            temp.next=Node(1)
        head=self.reverse(head.next)
        return head 





first = LinkList()
first.insertNodeatEnd(7)
first.insertNodeatEnd(7)
first.insertNodeatEnd(0)
first.insertNodeatEnd(3)
first.insertNodeatEnd(2)



second = LinkList()
second.insertNodeatEnd(2)
second.insertNodeatEnd(9)
second.insertNodeatEnd(6)
second.insertNodeatEnd(6)
second.insertNodeatEnd(0)

add=LinkList()

add.head=add.addNumbers(first.head, second.head)
add.printList()

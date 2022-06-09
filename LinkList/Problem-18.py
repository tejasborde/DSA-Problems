import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


#Check if singly Link List is Palindrome or not


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


left=None

def checkPalindrome(right):
    global left
    if(right==None):
        return True 
    
    previousAns=checkPalindrome(right.next)
    if(previousAns==False):
        return False
    
    ans=(left.data==right.data)
    left=left.next 

    return ans 


# Using Stack
# def isPalindrome(self, head):
#     stack=[]
#     start=head
#     while(start!=None):
#         stack.append(start.data)
#         start=start.next 
    
#     start=head 
#     while(start!=None):
#         if(start.data!=stack[-1]):
#             return 0
#         stack.pop()
#         start=start.next 
#     return 1

l=LinkList()

l.insertNodeatEnd(1)
l.insertNodeatEnd(23)
l.insertNodeatEnd(20)
l.insertNodeatEnd(2)
l.insertNodeatEnd(1)
left=l.head
print(checkPalindrome(l.head))

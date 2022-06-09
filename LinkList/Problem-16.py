import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


#Check if linklist is circular or not

# def isCircular(head):
#     if(head==None):
#         return 0
#     s=set()
#     while(head!=None):
#         if(head in s):
#             return 1
#         s.add(head)
#         head=head.next
#     return 0


def isCircular(head):
    if(head==None):
        return 0
    node=head
    while(node!=head and node!=None):
        node=node.next
    return (node==head)
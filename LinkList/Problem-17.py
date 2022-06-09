import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


# Split a Circular Linked List into two halves(two Circular List)
# Input:
# Circular LinkedList: 1->5->7
# Output:
# 1 5
# 7

   # S F
# 1,5,7



# Input:
# Circular LinkedList: 2->6->1->5
# Output:
# 2 6
# 1 5

#  S   F
#2 6 1 5


#Solution using Two Pointer Method


def splitList(self, head, head1, head2): 
        slow=head
        fast=head
        
        while(fast.next!=head and fast.next.next!=head):
            slow=slow.next
            fast=fast.next.next
            
        head1=head
        
        if(fast.next.next==head):
            fast=fast.next
        
        head2=slow.next 
        
        fast.next=slow.next
        slow.next=head1

        return head1,head2
#Reverse Doubly LinkList

def reverseDLL(head):
    if(head):
        temp=None
        cur=head
        
        while(cur):
            temp=cur.prev
            cur.prev=cur.next
            cur.next=temp
            cur=cur.prev
        if(temp):
            return temp.prev
        return head
    return head

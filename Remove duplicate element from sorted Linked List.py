
#Function to remove duplicates from sorted linked list.

def removeDuplicates(head):
    tail=head
    while tail!=None and tail.next!=None:
        if tail.data==tail.next.data:
            tail.next=tail.next.next
        else:
            tail=tail.next
    return head
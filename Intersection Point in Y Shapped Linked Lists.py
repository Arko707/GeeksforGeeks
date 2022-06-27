
def intersetPoint(head1,head2):
    ptr1 = head1
    ptr2 = head2
    if(ptr1 is None or ptr2 is None):
        return -1
    while(ptr1!=ptr2):
        ptr1 = ptr1.next
        ptr2 = ptr2.next
        if(ptr1==ptr2):
            return ptr1.data
        elif(ptr1==None):
            ptr1 = head2
        elif(ptr2==None):
            ptr2 = head1
        elif(ptr1==None and ptr2==None):
            return -1
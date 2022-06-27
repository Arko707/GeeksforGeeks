
#Function to find the data of nth node from the end of a linked list
def getNthFromLast(head,n):
    count = 0
    i = head
    while(i):
        count+=1
        i = i.next
        
    if n > count:
        return -1
        
    c =  count - n
    
    j = head
    
    for i in range(c):
        j = j.next
        
    return j.data
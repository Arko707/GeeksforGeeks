
class Solution:
    #Function to rotate a linked list.
    def rotate(self, head, k):
        curr=head
        size=0
        while curr.next!=None:
            size+=1
            curr=curr.next
        size+=1
        if size<k:
            return -1
        elif size==k:
           return head
        end=curr
        start=head
        curr=head
        pre=None
        while k>0:
            pre=curr
            curr=curr.next
            k-=1
        pre.next=None
        res=curr
        end.next=start
        return res
class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        t=head;u=head;
        while  t!=None and t.next!=None :
            u=u.next
            t=t.next.next
            if u==t:
                return True
        return False
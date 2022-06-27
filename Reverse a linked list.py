class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        prev = None
        p = head
        while p:
            temp = p.next
            p.next = prev
            prev = p 
            p = temp
        return prev
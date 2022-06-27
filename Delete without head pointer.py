
class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,curr):
        prev = None
        while(curr.next!=None):
            curr.data = curr.next.data
            prev = curr
            curr = curr.next
        prev.next = None
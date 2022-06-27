
class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        temp=head
        a=set()
        while temp:
            if temp.next not in a:
                a.add(temp)
            else:
                temp.next=None
                break
            temp=temp.next
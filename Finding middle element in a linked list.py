
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        temp= head
        count=0
        while temp!=None:
            count+=1 
            temp=temp.next
        temp=head
        mid=count//2
        while mid!=0:
            temp=temp.next 
            mid-=1
        return temp.data
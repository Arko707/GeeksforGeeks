
def checkpalindrome(l):
    l1=l[::-1]
    if(l==l1):
        return 1
    else:
        return 0

#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        h=head
        l=[]
        while(h is not None):
            l.append(h.data)
            h=h.next
            
        re=checkpalindrome(l)
        return re
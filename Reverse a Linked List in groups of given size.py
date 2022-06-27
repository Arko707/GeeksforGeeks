
class Solution:
    def reverse(self,head, k):
        a=[]
        temp=head
        while temp!=None:
            a.append(temp.data)
            temp=temp.next
        c=[]
        j=0
        j1=k
        for i in range(len(a)//k+1):
            a11=a[j:j1]
            a1=a11[::-1]
            for item in a1:
                c.append(item)
            j=j+k
            j1=j1+k 
            if j1>len(a):
                j1=len(a) 
        temp=head
        i=0
        while temp!=None:
            temp.data=c[i]
            i=i+1
            temp=temp.next 
        return head
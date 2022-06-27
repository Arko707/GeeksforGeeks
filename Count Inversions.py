
class Solution:
    #User function Template for python3
    c=0

    def merge(self,arr,l,m,r):
        a1=arr[l:m+1]
        a2=arr[m+1:r+1]
        x,y=m-l+1,r-m
        i,j,k=0,0,l
        while i<x and j<y:
            if a1[i]>a2[j]:
                self.c+=x-i
                arr[k]=a2[j]
                j+=1
            else:
                arr[k]=a1[i]
                i+=1
            k+=1
        while i<x:
            arr[k]=a1[i]
            i+=1
            k+=1
        while j<y:
            arr[k]=a2[j]
            j+=1
            k+=1
    
    def mergesort(self,arr,l,r):
        if l<r:
            m=(l+r)//2
            self.mergesort(arr,l,m)
            self.mergesort(arr,m+1,r)
            self.merge(arr,l,m,r)
    
    def inversionCount(self, arr, n):
        self.mergesort(arr,0,n-1)
        return self.c
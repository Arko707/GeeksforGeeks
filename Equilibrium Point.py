
class Solution:
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        sum=0
        for i in A:
            sum=sum+i
        tem=0
        for i in range(0,N):
            if((2*tem+A[i])==sum):
                return (i+1)
            tem=tem+A[i]
        return -1
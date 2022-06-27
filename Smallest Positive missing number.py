
class Solution:
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        t=1
        arr.sort()
        for i in range(0,n):
            if arr[i]==t:
                t=t+1
        return t
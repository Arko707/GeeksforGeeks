
class Solution:
    def majorityElement(self, A, N):
        maxx =  max(A)
        arr = [0 for i in range(maxx+1)]
        for i in A:
            arr[i] += 1
        
        b = max(arr)
        if b > (N)//2:
            return arr.index(b) 
        else:
            return -1

class Solution:
    def findTwoElement( self,arr, n): 
        for i in range(n):
            if arr[abs(arr[i])-1] < 0:
                repeating = abs(arr[i])
                continue
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
        for i in range(n):
            if arr[i] > 0:
                missing = i+1
                break
        return repeating, missing
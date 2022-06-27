
class Solution:
    def getMinDiff(self, arr, n, k):
        if n == 1:
            return 0
            
        arr.sort()
        
        max1, min1 = 0, 0
        
        diff = arr[n-1] - arr[0]
        
        for i in range(1, n):
            if (arr[i] -k) < 0:
                continue
            
            max1 = max(arr[i-1]+k, arr[n-1]-k)
            
            min1 = min(arr[0]+k, arr[i]-k)
            
            diff = min(diff, max1-min1)
            
        return diff
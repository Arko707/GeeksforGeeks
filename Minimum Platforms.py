
class Solution:    
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        res,j=1,0
        for i in range(1,n):
            if dep[j]>=arr[i]:
                res+=1
            else:
                j+=1
        return res
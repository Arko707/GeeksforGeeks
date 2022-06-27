
from collections import Counter
class Solution:
    def getPairsCount(self, arr, n, k):
        count=0
        d=Counter(arr)
        for i in d.keys():
            if i<k:
                if (k-i) in d.keys() and (k-i)!=i:
                    count+=d[i]*d[k-i]
                elif (k-i) in d.keys():
                    count+=d[i]*(d[i]-1)
        return count//2
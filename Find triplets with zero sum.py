
class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        arr.sort()
        mydict = {}
        
        for i in range(n):
            if arr[i] not in mydict:
                mydict[arr[i]] = 1
            else:
                mydict[arr[i]] += 1
                
        for i in range(n-2):
            for j in range(i+1, n-1):
                mydict[arr[i]] -= 1
                mydict[arr[j]] -= 1
                val = arr[i] + arr[j]
                valInv = -val
                if valInv in mydict:
                    if mydict[valInv] != 0:
                        return True
                mydict[arr[i]] += 1
                mydict[arr[j]] += 1
                
        return False
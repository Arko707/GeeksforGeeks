
class Solution:
    def findLongestConseqSubseq(self,arr, N):
        arr = set(arr)
        arr = list(arr)
        N = len(arr)
        arr.sort()
        max_len = 1
        temp = 1
        for i in range(1, N):
            if arr[i] - arr[i - 1] != 1:
                temp = 1
                max_len = max(max_len, temp)
                continue
            temp += 1
            max_len = max(max_len, temp)
        return max_len
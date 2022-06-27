
class Solution:
    def kthSmallest(self,arr, l, r, k):
        arr = sorted(arr)
        return arr[k-1]
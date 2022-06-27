#User function Template for python3

class Solution:
    def maxSubArraySum(self,arr,N):
        m = float('-inf')
        s = 0
        for i in range(0, N):
            if s + arr[i] < arr[i]:
                s = arr[i]
            else:
                s += arr[i]
            m = max(m,s)
        return m
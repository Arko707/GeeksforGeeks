
class Solution:
    def leaders(self, A, N):
        ma=A[N-1]
        i=N-2
        l=[ma]
        for i in range(N-2,-1,-1):
            if ma<=A[i]:
                ma=A[i]
                l.append(A[i])
        return l[::-1]

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
   def subArraySum(self,arr, n, s):
        start=0
        A=[]
        curr_sum=arr[0]
        i=1
        while i<=n:
            while curr_sum>s:
                curr_sum=curr_sum-arr[start]
                start+=1
            if curr_sum==s:
                A.append(start+1)
                A.append(i)
                return A
            if i<n:
                curr_sum=curr_sum+arr[i]
            i+=1
        A.append(-1)
        return A
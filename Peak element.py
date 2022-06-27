class Solution:   
   def peakElement(self,arr, n):
       
       def binarySearch(left, right, arr):
           mid = ((left + right) // 2)
           
           if left >= right:
               return left
               
           if arr[mid] < arr[mid + 1]:
               return binarySearch(mid + 1, right, arr)
           else:
               return binarySearch(left, mid, arr)
               
               
       return binarySearch(0, n - 1, arr)
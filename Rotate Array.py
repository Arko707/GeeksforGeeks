
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
       ll=A.copy()
       if D<N:
           ll=A[D:N]+A[0:D]
       else:    
             k=int(D/N)
             while k>=1:
                  ll=ll[D:N]+ll[0:D]
                  k=k-1
             r=D%N
             if r!=0:
                 ll=ll[r:N]+ll[0:r]
       A.clear()
       A.extend(ll)
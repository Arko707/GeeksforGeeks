
class Solution:
    def MissingNumber(self,array,n):
        total = (n+1)*n//2;
        total_a = sum(array);
        return total-total_a

class Solution:
    def maxProduct(self,arr, n):

        _min = arr[0]
        _max = arr[0]
        
        
        max_product = _max
        
        for i in range(1, n):
            curr_num = arr[i]
            
            temp_min = _min
            
            _min = min(curr_num, _max * curr_num, _min * curr_num)
            _max = max(curr_num, _max * curr_num, temp_min * curr_num)
            
            max_product = max(max_product, _max)
           
        return max_product
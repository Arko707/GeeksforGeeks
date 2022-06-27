
class Solution:
    
    #Function to return the diameter of a Binary Tree.
    def solve_diameter(self, root):
        if root is None:
            p = (0,0)
            return p
            
        right = self.solve_diameter(root.right)
        left = self.solve_diameter(root.left)
        
        op1 = right[0]
        op2 = left[0]
        op3 = right[1] + left[1] +1
        
        first = max(op1, op2, op3)
        second = max(right[1], left[1]) + 1
        ans = (first, second)
        return ans
        
        
        
    def diameter(self,root):
        return self.solve_diameter(root)[0]
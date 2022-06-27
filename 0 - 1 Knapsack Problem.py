
class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapsackDP(self, W, wt, val, n):
        dp = [[0 for i in range(W+1)] for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, W+1):
                if wt[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], val[i-1]+dp[i-1][j-wt[i-1]])
        return dp[n][W]
        
    def knapsackUtil(self, wt, val, W, curr_wt, curr_val, n, i):
        if i == n or n == 0:
            return curr_val
        if curr_wt + wt[i] > W:
            return self.knapsackUtil(wt, val, W, curr_wt, curr_val, n, i+1)
        else:
            return max(
                self.knapsackUtil(wt, val, W, curr_wt+wt[i], curr_val+val[i], n, i+1),
                self.knapsackUtil(wt, val, W, curr_wt, curr_val, n, i+1))
        
    def knapSack(self,W, wt, val, n):
        return self.knapsackDP(W, wt, val, n)
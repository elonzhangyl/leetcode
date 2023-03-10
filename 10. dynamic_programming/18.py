class Solution:
    def unboundied_knapsack(self, weight, value, cap):
        # Define dp
        dp = [[0 for _ in range(cap + 1)] for _ in range(len(weight))]

        # Initialize dp
        for j in range(cap + 1):
            dp[0][j] = weight[0] * j

        for i in range(len(weight)):
            for j in range(cap + 1):
                if j >= weight[i]:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - weight[i]] + value[i])
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp
    
print(Solution().unboundied_knapsack([1,2,4], [5,20,30], 4))


        


class Solution:
    def myfun(self, n):
        dp = [0] * n
        dp[0] = 0
        dp[1] = 1
        def backtracing():
            dp[i - 1] + dp [i - 2]
            return 
            
        for i in range(2, 30):
            fb[i] = fb[i - 1] + fb[i - 2]
        return fb
    
print(Solution().myfun())

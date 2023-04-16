class Solution:
    def maxUncrossedLines(self, nums1, nums2) -> int:
        res = 0
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    res = max(res, dp[i][j])
        return dp
print(Solution().maxUncrossedLines([3,3],[3]))
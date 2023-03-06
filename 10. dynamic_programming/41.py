nums = [7,7,7,7,7,7,7]
# dp[i] the length of the longest sub-sequence with ending nums[i]

dp = [1] * (len(nums) + 1)
for i in range(1, len(nums)):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(dp[i])
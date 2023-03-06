nums =  [2,2,2,2,2]
# dp[i] the length of the longest sub-sequence with ending nums[i]

dp = [1] * (len(nums))
for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = dp[i - 1]
        # print(f"i = {i}, dp = {dp}")
print(dp[i])
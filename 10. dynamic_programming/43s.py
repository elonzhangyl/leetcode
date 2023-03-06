# dp[i][j] means the length of the longest identical sub-sequence of A ending with A[i]
#  and sub-sequence B ending with B[j]
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
dp = [[0] * (len(nums2)+1) for _ in range((len(nums1)+1))]
for i in range(len(nums1)+1):
    for j in range(len(nums2)+1):
        if nums1[i-1] == nums2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        print(f"i = {i}, j = {j}, dp = {dp}")

print(dp)

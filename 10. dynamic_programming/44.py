# dp[i][j] means the length of the longest identical sub-sequence of A ending with A[i]
#  and sub-sequence B ending with B[j]
text1 = "abcde"
text2 = "ace"
dp = [[0] * (len(text2)+1) for _ in range((len(text1)+1))]
for i in range(1, len(text1)+1):
    for j in range(1, len(text2)+1):
        if text1[i-1] == text2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(f"i = {i}, j = {j}, dp = {dp}")

print(dp)

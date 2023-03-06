def num_set():
    set = [1, 5, 11, 5]
    c = int(sum(set)/2)

    dp = [0]*(c+1)
    for i in range(len(set)):
        print(i)
        for j in range(c, set[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - set[i]] + set[i])
        print(dp)
    
    return dp

dp = num_set()
print(dp)
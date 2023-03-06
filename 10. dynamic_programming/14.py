def last_stone():
    w = [2,7,4,1,8,1]
    c = int(sum(w)/2)

    dp = [0] * (c+1)
    for i in range(len(w)):
        for j in range(c, w[i]-1, -1):
            dp[j] = max(dp[j], dp[j - w[i]]+w[i])

    return abs(dp[-1]-(sum(w)-dp[-1]))

print(last_stone())
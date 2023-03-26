class Solution:
    def __init__(self):
        self.sum = 0
        self.path = []
        self.res = float('inf')

    def coinChange(self, coins, amount):
        recorder = [float('inf')] * (amount + 1)
        self.traverse(coins, amount, recorder)
        if self.res == float('inf'):
            self.res = -1
        return self.res

    def dp(self, coins, amount, recorder):
        if self.sum == amount:
            self.res = min(self.res, len(self.path[:]))
            return self.res
        elif self.sum > amount:
            return -1
        for i in range(len(coins)):
            self.sum += coins[i]
            self.path.append(coins[i])
            if self.sum < len(recorder):
                if recorder[self.sum] != float('inf'):
                    return recorder[self.sum]
                else:
                    recorder[self.sum] = self.dp(coins, amount, recorder)
            self.path.pop()
            self.sum -= coins[i]

print(Solution().coinChange([2,5,1], 11))
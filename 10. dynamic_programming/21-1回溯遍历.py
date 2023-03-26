class Solution:
    def __init__(self):
        self.sum = 0
        self.path = []
        self.res = float('inf')

    def coinChange(self, coins, amount):
        self.traverse(coins, amount)
        if self.res == float('inf'):
            self.res = -1
        return self.res

    def traverse(self, coins, amount):
        if self.sum == amount:
            self.res = min(self.res, len(self.path[:]))
            return self.res
        elif self.sum > amount:
            return -1
        for i in range(len(coins)):
            self.sum += coins[i]
            self.path.append(coins[i])
            self.traverse(coins, amount)
            self.path.pop()
            self.sum -= coins[i]

print(Solution().coinChange([2,5,1], 11))
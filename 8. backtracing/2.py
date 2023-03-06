class Solution:
    def __init__(self):
        self.path = []
        self.res = []
        self.iter = 0

    def combination(self, n, k):
        self.backtracking(list(range(1,n+1)), k, 0)
        return self.res

    def backtracking(self, nums, k, start):
        if start > len(nums): #这一步是防止超出索引范围而报错
            return
        if self.iter >= k: #这一步是控制层数
            self.res.append(self.path[:])
            return

        for i in range(start, len(nums)):
            self.path.append(nums[i])
            self.iter += 1
            self.backtracking(nums, k, i + 1)
            self.path.pop()
            self.iter -= 1

print(Solution().combination(4,2))
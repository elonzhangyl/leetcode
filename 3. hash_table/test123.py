class Solution:
    def reverse(self, t):
        left, right = 0, len(t) - 1
        while left < right:
            t[left], t[right] = t[right], t[left]
            left += 1
            right -= 1
        return t
    def cutting(self, nums, k):
        res= []
        nums = list(nums)
        for i in range(0, len(nums), 2 * k):
            res[i: i + 2 * k] = (self.reverse(nums[i: i + 2 * k]))
        return ''.join(res)

#         输入: s = "abcdefg", k = 2
# 输出: "bacdfeg"
print(Solution().cutting('abcdefg', 2))
# [-1, 0, 1, 2, -1, -4]，

# 满足要求的三元组集合为： [ [-1, 0, 1], [-1, -1, 2] ]
        
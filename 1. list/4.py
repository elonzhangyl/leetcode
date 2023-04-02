class Solution:
    def sq(self, nums):
        left, right = 0, len(nums) - 1
        res = [0] * len(nums)
        idx = len(nums) - 1
        while left <= right:
            lv, rv = nums[left]**2, nums[right]**2
            if lv > rv:
                res[idx] = lv
                left += 1
            else:
                res[idx] = rv
                right -= 1
            idx -= 1
        return res
print(Solution().sq([-4,-1,0,3,10]))

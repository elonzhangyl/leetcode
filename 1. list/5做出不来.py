class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        left, right = 0, 0
        res = float('inf')
        sum_ = 0
        for right in range(len(nums)):
            sum_ += nums[right]
            while sum_ >= target:
                res = min(res, right - left + 1)
                sum_ -= nums[left]
                left += 1
        return res if res != float('inf') else 0
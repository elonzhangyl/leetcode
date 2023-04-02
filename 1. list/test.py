class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        left, right = 0, 0
        res = float('inf')
        sub_nums = 0
        while left <= right < len(nums):
            if sub_nums < target:
                sub_nums += nums[right]
                if sub_nums >= target:
                    res = min(res, right - left + 1)
                right += 1
            elif sub_nums >= target:
                res = min(res, right - left + 1)
                sub_nums -= nums[left]
                left += 1
        return res if res != float('inf') else 0
    
print(Solution().minSubArrayLen(15, [1,2,3,4,5]))
# print(Solution().minSubArrayLen(4, [1,4]))


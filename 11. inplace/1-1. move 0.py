# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]

class Solution:
    def move_zero_to_end(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            left += 1
        return nums
    
print(Solution().move_zero_to_end([0,1,0,3,12]))
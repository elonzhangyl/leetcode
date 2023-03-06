# 暴力
class Solution:
    def remove_element(self, nums, target):
        res = {}
        k = 0
        for i in range(len(nums)):
            if nums[i] == target:
                for j in range(i, len(nums) - 1):
                    nums[j] = nums[j + 1]
        
        return nums[0:i]

print(Solution().remove_element([0,1,2,2,3,0,4,2], 2))
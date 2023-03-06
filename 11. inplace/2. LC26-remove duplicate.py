# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# 输入：nums = [0,0,1,1,1,2,2,3,3,4]
# 输出：5, nums = [0,1,2,3,4]
class Solution:
    def remove_duplicates(self, nums):
        i, j = 0, 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
                j += 1
        return nums  

print(Solution().remove_duplicates([0,0,1,1,1,2,2,3,3,4]))            
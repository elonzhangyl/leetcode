# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]

class Solution:
    def move_zero_to_end(self, nums):
        count = 0
        for num in nums:
            if num == 0:
                count += 1
        
        return nums
    
print(Solution().move_zero_to_end([0,1,0,3,12]))
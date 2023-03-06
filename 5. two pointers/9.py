class Solution:
    def three_sum(self, nums):
        res = []
        nums.sort()
        if nums[0] > 0:
                return False
        for i in range(len(nums)):
            if len(res) > 0 and res[-1][0] == nums[i]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                            left += 1
                    while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                    left += 1
                    right -= 1
                elif sum_ > 0:
                    right -= 1
                else:
                    left += 1

        return res
print(Solution().three_sum([-1, 0, 1, 2, -1, -4]))
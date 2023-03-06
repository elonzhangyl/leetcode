class Solution:
    def three_sum(self, nums, target):
        res = []
        nums.sort()
        if nums[0] > 0 and nums[0] > target:
            return False
        # elif nums[0] < 0 and nums[0] > target:
        #     return False
        for i in range(len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    sum_ = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum_ == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                                left += 1
                        while left < right and nums[right] == nums[right - 1]:
                                right -= 1
                        left += 1
                        right -= 1
                    elif sum_ > target:
                        right -= 1
                    else:
                        left += 1

        return res
print(Solution().three_sum([1, 0, -1, 0, -2, 2], 0))
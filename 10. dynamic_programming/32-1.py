nums = [7,1,5,3,6,4]
# [7,6,4,3,1]

# # very basic - how to find max in a list
# res = 0
# for num in nums:
#     res = max(res, num)
# print(res)

# brute force searching
# tip 1 - find max while looping
# tip 2 - inner traverse start from sensible values
profit = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        profit = max(profit, nums[j] - nums[i])
print(profit)
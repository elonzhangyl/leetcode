nums = [7,1,5,3,6,4]
# greedy algorithm
# sub-optimal make total optimal
def stock(nums):
    p_min = float('inf')
    profit = 0
    for i in range(len(nums)):
        p_min = min(p_min, nums[i])
        profit = max(profit, nums[i] - p_min)
    print(profit)

stock(nums)
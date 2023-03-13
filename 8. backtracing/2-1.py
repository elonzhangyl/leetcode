nums = [1,2,3]
res = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        res.append([nums[i], nums[j]])

print(res)

nums = [5]
target = 5

for x in range(0, len(nums)):
    if nums[x] == target:
        print(x)
        exit()
    elif nums[x] == nums[len(nums) - 1] and nums[x] != target:
        print(-1)

nums = [-1,0]
target = -1

def twoSum(nums, target):

    for x in range(0, len(nums)):
        for y in range(1, len(nums)):
            if nums[y] + nums[x] == target and y != x:
                return [x + 1, y + 1]

print(twoSum(nums, target))
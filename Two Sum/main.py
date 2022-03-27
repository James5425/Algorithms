nums = [2, 7, 11, 15]
target = 9


def twoSum(nums, target):
    dic = {}
    for x, y in enumerate(nums):
        key = target - y
        if key in dic:
            return [dic[key], x]
        else:
            dic[y] = x



print(twoSum(nums, target))



Wed Arvo 3:30 - 4:30
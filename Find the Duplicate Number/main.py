nums = [8, 1, 1, 9, 5, 4, 2, 7, 3, 6]


def LinearfindDuplicate(nums):
    for x in range(0, len(nums)):
        for y in range(1, len(nums)):
            if nums[x] == nums[y] and x != y:
                return nums[x]


def BinaryfindDuplicate(nums):
    nums.sort()

    for x in range(0, len(nums)):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[x] == nums[mid]:
                if x != mid:
                    return nums[x]
                else:
                    break
            elif nums[x] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1


print(BinaryfindDuplicate(nums))
print(LinearfindDuplicate(nums))

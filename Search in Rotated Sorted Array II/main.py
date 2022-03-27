nums = [1, 0, 1, 1, 1]
target = 0


def searchInSorted(nums, target):
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


print(searchInSorted(nums, target))

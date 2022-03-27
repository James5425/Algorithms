nums = [1,3]

target = 2

def search(arr, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:

            right = mid - 1

    return left


print(search(nums, target))

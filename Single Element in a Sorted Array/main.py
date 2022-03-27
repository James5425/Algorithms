nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]

def NotDuplicate(nums):
    for x in range(0, len(nums)):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == nums[x]:

print(NotDuplicate(nums))
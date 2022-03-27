nums = [1,2,3,1,1,3]

def number_of_good_pairs(nums):
    counter = 0

    for x in range(0, len(nums)):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == nums[x] and mid != x:
                counter += 1
                print(f"({x}, {mid})")
                break
            elif nums[mid] < nums[x]:
                left = mid + 1
            else:
                right = mid - 1
    return counter

def take_two(nums):
#print(number_of_good_pairs(nums))

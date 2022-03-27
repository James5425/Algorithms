import time
nums = [3,4,51,4,3, 0]

def find(nums):
    start = time.time()
    lst = []
    for x in range(1, len(nums) + 1):
        if x not in nums:
            lst.append(x)
    print(f"took {time.time() - start} seconds")
    return lst

def faster(nums):

    lst = []
    nums = sorted(nums)
    for x in range(1, len(nums) + 1):
        print(nums[0], x, nums[-1])
        if x < nums[0] or x > nums[-1]:
            lst.append(x)
    return lst

print(find(nums))
print(faster(nums))

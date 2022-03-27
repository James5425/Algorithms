nums = [1, 2, 3, 4]

def Sum(nums):
    start = nums[0]
    arr = []
    arr.append(start)
    for x in range(1, len(nums)):
        thing = nums[x]+ start
        arr.append(thing)
        start = thing

    return arr

print(Sum(nums))

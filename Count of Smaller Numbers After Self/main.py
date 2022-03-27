import time
nums = [7, 5, 6, 4]

def smaller(nums):
    start = time.time()
    res = []
    for x in range(0, len(nums)):
        counter = 0
        for y in range (0, len(nums)):
            if nums[x] > nums[y]:
                if x < y:
                    counter += 1
        res.append(counter)
    print(f"Time: {time.time() - start} and result = {res}")

def fast(nums):
    start = time.time()
    res = []
    for x in range(0, len(nums)):
        counter = 0
        for y in range(x + 1, len(nums)):
            if nums[x] > nums[y]:
                counter += 1
        res.append(counter)
    print(f"Time: {time.time() - start} and result = {res}")

def faster(nums):
    start = time.time()
    res = []

    for x in range(0, len(nums)):
        counter = 0
        for y in range(x + 1, len(nums)):
            if nums[x] > nums[y]
                counter += 1
        res.append(counter)
    print(f"Time: {time.time() - start} and result = {res}")

smaller(nums)
fast(nums)
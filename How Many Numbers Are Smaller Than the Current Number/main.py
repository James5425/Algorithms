nums = [7, 7, 7, 7]

def smaller(nums):
    res = []
    for x in nums:
        counter = 0
        for y in nums:
            if x > y:
                counter += 1
        res.append(counter)
    return res


print(smaller(nums))
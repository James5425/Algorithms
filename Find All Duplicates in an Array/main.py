nums = [4,3,2,7,8,2,3,1]

def remove(nums):
    dic = {}
    new = []
    for x in nums:
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] = dic[x] + 1
    for y, z in dic.items():
        if z > 1:
            new.append(y)
    return sorted(new)

print(remove(nums))
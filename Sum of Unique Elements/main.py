nums = [1, 2, 3, 2]

def sum_of_unique_elements(nums):
    tot = 0
    if set(nums) == nums:
        return sum(nums)
    else:
        dic = {}
        for x in nums:
            if x not in dic:
                dic[x] = 1
            else:
                dic[x] += 1

        for key, value in dic.items():
            if value == 1:
                tot += key

        return tot



print(sum_of_unique_elements(nums))
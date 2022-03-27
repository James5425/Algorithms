nums = [0,0,1,1,1,2,2,3,3,4]
soughted = []

def removeDuplicates(nums):
    for x in nums:
        if x not in soughted:
            soughted.append(x)
    print(soughted)

removeDuplicates(nums)


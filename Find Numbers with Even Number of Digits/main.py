nums = [12, 345, 2, 6, 7896]
even = 0
for x in nums:
    length = len(str(x))
    if (length % 2) == 0:
        even += 1

print(even)
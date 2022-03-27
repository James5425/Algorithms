nums = [1,0,1,1,0,1]
counts = []
count = 0


for x in nums:
    if x == 1:
        count += 1
    elif x != 1:
        counts.append(count)
        count = 0

counts.append(count)

max = counts[0]
for num in counts:
    if num > max:
        max = num

print(counts)
print(max)

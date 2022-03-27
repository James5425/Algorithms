array = [4,5,6,7,0,1,2]
target = 0

ordered = []
while array:
    lowest = array[0]
    for i in array:
        if i < lowest:
            lowest = i
    ordered.append(lowest)
    array.remove(lowest)

left = 0
right = len(ordered)

while left <= right:
    mid = (left + right) // 2
    if ordered[mid] == target:
        print(mid)
    elif ordered[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

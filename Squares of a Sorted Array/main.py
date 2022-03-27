#This works but doesn't follow the time complexity of O(n)

nums = [-4,-1,0,3,10]
squared = []
ordered = []


for x in nums:
    squared_num = (x ** 2)
    squared.append(squared_num)

while squared:
    lowest = squared[0]
    for i in squared:
        if i < lowest:
            lowest = i
    ordered.append(lowest)
    squared.remove(lowest)


    print(squared)
    print(ordered)
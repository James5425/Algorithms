array = [9, 2, 4, 23 ,1]

ordered = []
while array:
    lowest = array[0]
    for i in array:
        if i < lowest:
            lowest = i
    ordered.append(lowest)
    array.remove(lowest)
print(ordered)







array1 = [4, 5, 1, 4, 5, 9, 0, 11, 23, 3, 1, 1, 3, 5]
array2 = [3, 5, 6, 8, 1, 4, 3, 1, 10, 11, 9]
array = []
ordered = []

def addArrays(): #combine arrays
    for i in array1:
        array.append(i)
    for x in array2:
        array.append(x)

def order(): #order array

    while array:
        lowest = array[0]
        for i in array:
            if i < lowest:
                lowest = i
        ordered.append(lowest)
        array.remove(lowest)
    print(ordered)

def findMedian(): #find median of combine array
    length = len(ordered)
    if length % 2 == 0:
        median1 = ordered[length // 2]
        median2 = ordered[length // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = ordered[length // 2]
    print("Median is: " + str(median))

if __name__ == '__main__':
    addArrays()
    order()
    findMedian()


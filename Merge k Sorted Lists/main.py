lists = [[1,4,5],[1,3,4],[2,6]]

def mergeKLists(list):
    single = []

    for x in list:
        for j in x:
            single.append(j)
            list.remove(j)

    low = single[0]
    while single:
        for y in single:
            if y < low:
                low = y
            list.append(low)
            print(list)
            single.remove(low)

    print(list)


mergeKLists(lists)
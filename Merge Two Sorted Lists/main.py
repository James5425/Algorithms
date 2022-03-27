list1 = [1, 2, 4]
list2 = [1, 3, 4]

def merge(l1, l2):
    l3 = []
    while l1 and l2:
        if l1[0] < l2[0]:
            l3.append(l1.pop(0))
        else:
            l3.append(l2.pop(0))
    l3.extend(l1)
    l3.extend(l2)
    return l3

print(merge(list1, list2))


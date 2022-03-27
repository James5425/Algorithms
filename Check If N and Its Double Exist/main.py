arr = [-2,0,10,-19,4,6,-8]

def checkIfExist(arr):
    for x in arr:
        if x / 2 in arr:
            return True
    return False

print(checkIfExist(arr))

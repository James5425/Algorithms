matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

def search(matrix, target):
    for x in matrix:
        if target in x:
            return True
    return False

print(search(matrix, target))
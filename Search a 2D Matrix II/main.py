matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20

def search(matrix, target):
    for x in matrix:
        if target in x:
            return True
    return False

print(search(matrix, target))
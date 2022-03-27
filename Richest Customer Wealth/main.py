accounts = [[1,2,3],[3,2,1]]

def Richest(accounts):
    max = 0

    for x in accounts:
        sum = 0
        for y in x:
           sum = sum + y

        if sum > max:
            max = sum

    return max



print(Richest(accounts))
n = 4

def climb(n):
    m = 0
    y = 1
    for i in range(2, n + 2):
        o = m + y
        m = y
        y = o
    return y

print(climb(n))
n = 342

def find(n):
    m = 0
    y = 1
    for i in range(2, n + 1):
        o = m + y
        m = y
        y = o
    return y

print(find(n))
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

def ans(s, indices):
    res = [''] * len(s)
    for i, c in enumerate(s):
        res[indices[i]] = c
    return ''.join(res)


print(ans(s, indices))
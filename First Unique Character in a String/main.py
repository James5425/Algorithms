s = "leetcode"

def first(s):
    dic = {}
    for x in s:
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1
    for x, y in dic.items():
        if y == 1:
            return s.index(x)
    return -1

print(first(s))

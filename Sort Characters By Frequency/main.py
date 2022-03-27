s = "tree"

def sort(s):
    dic = {}
    ans = ''
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    dic = (dict(sorted(dic.items(), key=lambda item: item[1], reverse=True)))
    for x, y in dic.items():
        ans = ans + x * y
    return ans




print(sort(s))
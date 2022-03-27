s = "abcd"
t = "abcde"

def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    s_list = list(s)
    t_list = list(t)
    for i in range(len(s_list)):
        if s_list[i] != t_list[i]:
            return t_list[i]
    return t_list[-1]

print(findTheDifference(s, t))
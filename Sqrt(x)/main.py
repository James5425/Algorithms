def squrt(x):
    lower = 0
    upper = x
    while lower <= upper:
        mid = (upper + lower) // 2
        dist = x - (mid * mid)
        if dist > 0:
            if (mid + 1) * (mid + 1) > x:
                return mid
            lower = mid + 1
        elif dist < 0:
            upper = mid - 1
        else:
            return mid
    return mid

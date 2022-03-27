def isPerfectSquare(num):
    low = 0
    high = num

    while low <= high:
        mid = (low + high) // 2
        if mid ** 2 == num:
            return True
        elif mid ** 2 < num:
            low = mid + 1
        else:
            high = mid - 1
    return False

print(isPerfectSquare(16))
import time
low = 1
high = 11

def odd(low, high):
    start = time.time()
    counter = 0
    for x in range(low, high + 1):
        if x % 2 != 0:
            counter += 1
    print(counter)
    return f"loop took {time.time() - start} seconds"

def fast(low, high):
    start = time.time()
    if low % 2 != 0 and high % 2 != 0:
        return (high - low) // 2 + 1
    elif low % 2 == 0 and high % 2 == 0:
        return (high - low) // 2
    else:
        print((high - low + 1) // 2)

    return f"loop took {time.time() - start} seconds"


print(fast(low, high))
print(odd(low, high))
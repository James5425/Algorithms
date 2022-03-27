jewels = "aA"
stones = "aAAbbbb"

def jewelery(jewels, stones):
    counter = 0

    if len(jewels) == 0:
        return 0

    for x in jewels:
        for y in stones:
            if x == y:
                counter += 1
    return counter
print(jewelery(jewels, stones))
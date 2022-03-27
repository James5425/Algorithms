candies = [2, 3, 5, 1, 3]
extraCandies = 3

def extra(candies, extraCandies):
    arr = []
    max_candies = max(candies)

    for x in candies:
        if x + extraCandies >= max_candies:
            arr.append(True)
        else:
            arr.append(False)

    return arr

def faster(candies, extraCandies):
    cut = max(candies) - extraCandies
    return [x >= cut for x in candies]
    #return [x + extraCandies >= max(candies) for x in candies]

print(faster(candies, extraCandies))
#print(extra(candies, extraCandies))


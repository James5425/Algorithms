heights = [1, 1, 4, 2, 1, 3]


def heightChecker(heights):
    expected = heights.copy()
    expected.sort()
    k = len(heights)
    count = 0
    for i in range(0, k):
        if (expected[i] != heights[i]):
            count = count + 1
    return count


print(heightChecker(heights))

n = 11111111111111111111111111111101
def hammingWeight(n):
    n = str(n)
    count = 0
    for x in n:
        if x == "1":
            count += 1

    return count

print(hammingWeight(n))

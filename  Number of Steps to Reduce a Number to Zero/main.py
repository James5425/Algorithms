num = 8

def steps(num):
    counter = 0
    while num != 0:
        if num % 2 == 0:
            num = num / 2
            counter += 1
        else:
            num = num - 1
            counter += 1
    return counter

print(steps(num))
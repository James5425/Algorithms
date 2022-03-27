n = 4421

sum1 = 0
sum = 1
for x in str(n):
    sum = sum * int(x)
    sum1 = sum1 + int(x)

print(sum - sum1)


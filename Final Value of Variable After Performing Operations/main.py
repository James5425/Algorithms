operations = ["++X","++X","X++"]
num = 0
for x in operations:
    if "-" in x:
        num -= 1
    else:
        num += 1

print(num)
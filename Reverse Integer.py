def answer(i):
    nums = str(i)

    if nums[0] == '-':
        print(int('-'+nums[:0:-1]))
    else:
         print(int(nums[::-1]))

number = input("Enter an Integer to Reverse\n>")
answer(number)

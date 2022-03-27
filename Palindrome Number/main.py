x = -121

def isPalindrome(x):
    nums = str(x)

    try:
        if (int(nums[::-1])) == x:
            return True
        else:
            return False
    except ValueError:
        return False

print(isPalindrome(x))
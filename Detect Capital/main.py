word = "USA"

def upper(word):
    if word == word.upper():
        return True
    elif word == word.capitalize():
        return True
    elif word == word.lower():
        return True
    else:
        return False

print(upper(word))
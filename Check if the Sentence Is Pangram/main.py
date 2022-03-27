sentence = "hxsdz"

def Pangram(sentence):
    if "a" and "b" and "c" and "d" and "e" and "f" and "g" and "h" and "i" and "j" and "k" and "l" and "m" and "n" and "p" and "q" and "r" and "s" and "t" and "u" and "v" and "w" and "x" and "y" and "z" in sentence:
        return True

    elif "a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "i" or "j" or "l" or "m" or "n" or "p" or "q" or "r" or "s" or "t" or "u" or "v" or "w" or "x" or "y" or "z":
        return False

print(Pangram(sentence))
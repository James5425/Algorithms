sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

def max_num_word(sentences):
    longest = 0
    for x in sentences:
        length = len(x.split())
        if length > longest:
            longest = length

    return longest



print(max_num_word(sentences))
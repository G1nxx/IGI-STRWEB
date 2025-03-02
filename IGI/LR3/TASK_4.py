# Count quantity of words with min length in string
def Count_min_len(s) -> (int | int) :
    min_len = len(s)
    N = 0;
    words = s.replace(",","").replace(".","").split(' ')
    for word in words :
        if (len(word) == 0):
            continue
        elif (len(word) < min_len):
            N = 1
            min_len = len(word)
        elif (len(word) == min_len) :
            N += 1
    return (N, min_len)

# Count quantity of words with comma before them
def Count_words_before_comma(s) -> int :
    N = 0
    words = s.replace(".","").split(' ')
    for word in words :
        if (len(word) == 0):
            continue
        elif (word[-1] == ',') :
            N += 1
    return N

# Finds word in string with max length and which ends with letter, entered by user
def Find_max_word_with_end(s, c) -> str :
    max_len = 0
    max_word = ""
    words = s.replace(".","").replace(",","").split(' ')
    for word in words :
        if (len(word) <= max_len):
            continue
        elif (word[-1] == c) :
           max_word = word
           max_len = len(word)
    return max_word
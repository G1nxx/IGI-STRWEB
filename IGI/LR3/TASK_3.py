# This function count all word? which start whith lowercase letter.
def Count_lowercase_words(s) -> int:
    if type(s) is not str :
        raise Exception("Error! Value is not string")
    N = 0
    words = s.split(' ')
    for word in words :
        if len(word) > 0 :
          if word[0].islower() :
               N += 1
    return int(N)


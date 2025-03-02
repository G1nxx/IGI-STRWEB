from my_input import input_float

# This function count not negative digits. It stops when user enters digit less then -100.
def Count_not_negative() -> int:
    n = 0
    while True :
        print("Input digit: ")
        a = input_float()
        if a < -100 :
            break
        else :
            if a >= 0 :
                n += 1
    return n

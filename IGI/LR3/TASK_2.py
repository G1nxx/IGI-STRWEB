from my_input import input_float

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

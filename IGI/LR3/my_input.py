# This method is used to input string and check if is it a int value or not.
def input_int() -> int :
    _in = input()
    while True :
        if not _in.isdigit():
            _in = input("Incorrect input. Value is not integer. Input right value: ")
        else :
            break
    return _in

# This method is used to input string and check if it is a float value or not.
def input_float() -> float :
    _in = input()
    while True :
        if not _in.replace('.','',1).isdigit():
            _in = input("Incorrect input. Value is not digit. Input right value: ")
        else :
            break
    return _in
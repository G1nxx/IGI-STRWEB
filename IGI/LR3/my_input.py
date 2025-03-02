# This method is used to input string and check if is it a int value or not.
def input_int() -> int :
    is_neg = False
    _in = input()
    if (_in[0] == '-') :
        _in = _in[1:]
        is_neg = True
    while True :
        if not _in.isdigit():
            _in = input("Incorrect input. Value is not integer. Input right value: ")
        else :
            break
    return -int(_in) if is_neg else int(_in)

# This method is used to input string and check if it is a float value or not.
def input_float() -> float :
    is_neg = False
    _in = input()
    if (_in[0] == '-') :
        _in = _in[1:]
        is_neg = True
    while True :
        if not _in.replace('.','',1).isdigit():
            _in = input("Incorrect input. Value is not digit. Input right value: ")
        else :
            break
    return -float(_in) if is_neg else float(_in)
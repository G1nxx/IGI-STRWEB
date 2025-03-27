from random import random
import os

# This method is used to input string and check if is it a int value or not.
def input_int() -> int:
    is_neg = False
    _in = input()
    if (len(_in) != 0) :
        if (_in[0] == '-'):
            _in = _in[1:]
            is_neg = True
        else :
            is_neg = False
    while True :
        if not _in.isdigit():
            _in = input("Incorrect input. Value is not integer. Input right value: ")
            if (len(_in) != 0) :
                if (_in[0] == '-') :
                    _in = _in[1:]
                    is_neg = True
                else :
                    is_neg = False 
        else :
            break
    return -int(_in) if is_neg else int(_in)

# This method is used to input string and check if it is a float value or not.
def input_float() -> float:
    is_neg = False
    _in = input()
    if (len(_in) != 0) :
        if (_in[0] == '-'):
            _in = _in[1:]
            is_neg = True
        else :
            is_neg = False
    while True :
        if not _in.replace('.','',1).isdigit():
            _in = input("Incorrect input. Value is not digit. Input right value: ")
            if (len(_in) != 0) :
                if (_in[0] == '-') :
                    _in = _in[1:]
                    is_neg = True
                else :
                    is_neg = False                    
        else :
            break
    return -float(_in) if is_neg else float(_in)

# Returns text string for task 4
def collection_for_serialization():
    school_workload = [
        {"name": "Petrovich", "load": 10},
        {"name": "Stepan Andreich", "load": 8},
        {"name": "Anisimov", "load": 21},
        {"name": "SnapchatHack", "load": 13},
        {"name": "Pal Palich", "load": 3},
        {"name": "Som Palich", "load": 3}
    ]
    return school_workload;

# Creates array with random values 
def randomize(N: int) -> list[float]:
    arr = []
    for _ in range(N) :
        arr.append((random() - 0.5) * int(random() * 100))
    return arr

def input_color():
    _in = input()
    while True :
        match _in:
            case "red":
                return(_in)
            case "yellow":
                return(_in)
            case "green":
                return(_in)
            case "blue":
                return(_in)
            case "orange":
                return(_in)
            case "black":
                return(_in)
            case "pink":
                return(_in)
            case default:
                _in = input("Incorrect input. Value is not digit. Input right value: ")

if __name__ == '__main__':
    raise Exception("You can`t use this file as executable one");
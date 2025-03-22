from typing import Callable, List
from random import random

# This method is used to input string and check if is it a int value or not.
def input_int() -> int :
    is_neg = False
    _in = input()
    if (len(_in) != 0) :
        if (_in[0] == '-') :
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
def input_float() -> float :
    is_neg = False
    _in = input()
    if (len(_in) != 0) :
        if (_in[0] == '-') :
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
def text_to_parse() -> str :
    s = "So she was considering in her own mind, as well as she could, for the hot day made her feel "
    s += "very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble "
    s += "of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."
    return s;

# Creates array with random values 
def randomize(N: int):
    for _ in range(N) :
        yield ((random() - 0.5) * int(random() * 100))
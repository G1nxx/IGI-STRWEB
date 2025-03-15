
from my_input import *
from math import fabs

# Find summ betwine first and second positive in array.
def Find_sum(arr) -> float :
    sum = 0
    checker = False
    for i in range(len(arr)):
        if arr[i] > 0 :
            if checker == False :
                checker = True
                continue
            else :
                return sum
        if checker :
            sum += arr[i]

# Find max digit in array.
def Find_max_in_collection(arr) -> float:
    max = 0;
    for a in arr :
        if fabs(a) > fabs(max) :
            max = a
    return max

# Formated print of collection
def Print_collection(arr) :
    print("| ", end='')
    for a in arr :
        print(str(a), end=" | ")
    print()

# Input digits in array. User enters length of array. There is option to randomize array
def Input_collection() -> (float | float) :
    arr = []
    print("Enter capacity of array: ", end='')
    N = input_int()
    checker = input("Do you want to randomize collection? [y/n]: ")
    while True :
        if  checker.lower() == 'n' :
            for _ in range(N):
                print("Enter value: ", end='')
                el = input_float()
                arr.append(el)
            break
        elif checker.lower() != 'y' :
            print("Error!")
        else :
            gen = randomize(N)
            for _ in range(N) :
                arr.append(next(gen))
            break
        checker = input("do you want to continue? [y/n] ")
    sum = Find_sum(arr)
    max = Find_max_in_collection(arr)
    Print_collection(arr)
    return (sum, max)


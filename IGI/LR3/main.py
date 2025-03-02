from TASK_1 import Macloren_exp
from TASK_2 import Count_not_negative
from my_input import *

# Task 1. Main goal is to create method to evaluate exp(x) whith Tailor series and to print all information about this method.
def task1() :
    eps = 0.0001
    while True :
        print("Enter x: ", end='')
        x = input_float()
        res = Macloren_exp(float(x),eps)
        print("| {:<10} | {:<5} | {:<10} | {:<10} | {:<10} |"
                .format("x", "n", "Fx", "MATH_Fx", "eps"))
        print("-" * 60)
        print("| {:<10.7f} | {:<5} | {:<10.7f} | {:<10.7f} | {:<10.7f} |"
                .format(x, res[0], res[1], res[2], eps))
        break

def task2() :
    print("Start entering digits. Program will count all not negative one."
           + "Program stops, if you enter digit less then -100.")
    N = Count_not_negative()
    print("Count of not negative digits = " + str(N))

def task3() :
    print("Task3 is caled")

def task4() :
    print("Task4 is caled")

def task5() :
    print("Task5 is caled")

def task6() :
    print("Task6 is caled")

# main. This function is used to start tasks.
def main() :
    print("main is started")
    while True :
        print("Choose task from 1 to 6: ", end='')
        task = input_int()
        if (task > 6) | (task < 0) :
                print("Wrong input. Value must be in range from 1 to 6.")
        else :
            match (int(task)) :
                case 1:
                    task1()
                case 2:
                    task2()
                case 3:
                    task3()
                case 4:
                    task4()
                case 5:
                    task5()
                case 6:
                    task6()
            print ("main is ended")
            break

checker = 'y'
while True :
    if  checker == 'n' :
        break
    elif checker != 'y' :
        print("Error!")
    else :
        main()
    checker = input("do you want to continue? [y/n] ")
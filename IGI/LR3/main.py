"""
        This program is made by student Burchuck Dmitrij Aleksandrovich
        from group 353502. Date: 02.03.2025
        Main goal of this proram is to realize and show basick python
        entities and operations with them.
        Lab №3. Standart data types, collections, functions and modules.
"""
from TASK_1 import Macloren_exp
from TASK_2 import Count_not_negative
from TASK_3 import Count_lowercase_words
from TASK_4 import *
from TASK_5 import *
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

# Task 2. Main goal is to count not negative digits in sequense.
def task2() :
    print("Start entering digits. Program will count all not negative one."
           + "Program stops, if you enter digit less then -100.")
    N = Count_not_negative()
    print("Count of not negative digits = " + str(N))

# Task 3. Main goal is to count quantity of words with lowercase first letter
def task3() :
    s = input("Enter your string:\n")
    N = Count_lowercase_words(s)
    print("Count of not lowercase words = " + str(N))

# Task 4. Main goal is to parse text and to count some specific types of words in it, like
            # 1) quanity of words with min length
            # 2) quanity of words before comma
            # 3) word with max length, wich have 'y' at the end of it
def task4() :
    text = text_to_parse()
    subtask1 = Count_min_len(text)
    print("Count of words with min len = " + str(subtask1[0]) 
          + ", with len = " + str(subtask1[1]))
    subtask2 = Count_words_before_comma(text)
    print("Count of words with comma after them = " + str(subtask2) )
    subtask3 = Find_max_word_with_end(text,'y')
    print("Word with max len and 'y' at the end is: " + subtask3)

# Task 5. Main goal is to input collection of digits, printing them, finding max of them and finding max betwine 2 first positive digits.
def task5() :
    print("input your collection: ")
    result = Input_collection()
    print("Sum = " + str(result[0]))
    print("Max = " + str(result[1]))

# Realization of decorator. User interface.
def __strart_decorator(main_foo: Callable) :
    checker = 'y'
    while True :
        if checker.lower() == 'n' :
            break
        elif checker.lower() != 'y' :
            print("Error!")
        else :
            try :
                main_foo()
            except RuntimeError:
                print("Something went wrong while runtime.")
            except OverflowError:
                print("Owerflow error.")
            except Exception:
                print("Something went wrong. Exeption was thrown.")
        checker = input("do you want to continue? [y/n] ")
    exit()


# main. This function is used to start tasks.
@__strart_decorator
def main() :
    print("main is started")
    while True :
        print("Choose task from 1 to 5: ", end='')
        task = input_int()
        if (task > 5) | (task < 0) :
            print("Wrong input. Value must be in range from 1 to 5.")
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
            print ("main is ended")
            break

main()
"""
        This program is made by student Burchuck Dmitrij Aleksandrovich
        from group 353502. Date: 02.03.2025
        Main goal of this proram is to realize and show basick python
        entities and operations with them.
        Lab №3. Standart data types, collections, functions and modules.
"""
from my_input import *

# Task 1. Main goal is to 
def task1():
    pass

# Task 2. Main goal is to 
def task2():
    pass

# Task 3. Main goal is to
def task3():
    pass

# Task 4. Main goal is to p
def task4():
    pass

# Task 5. Main goal is to 
def task5():
    pass

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

if __name__ == '__main__':
    main()
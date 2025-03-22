"""
        This program is made by student Burchuck Dmitrij Aleksandrovich
        from group 353502. Date: 02.03.2025
        Main goal of this proram is to realize and show basick python
        entities and operations with them.
        Lab №3. Standart data types, collections, functions and modules.
"""
from my_input import *
from task_manager import *

# Realization of decorator. User interface.
def __strart_decorator(main_foo: callable) :
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
            manager = task_manager();
            match (int(task)) :
                case 1:
                    manager.task1()
                case 2:
                    manager.task2()
                case 3:
                    manager.task3()
                case 4:
                    manager.task4()
                case 5:
                    manager.task5()
            print ("main is ended")
            break

if __name__ == '__main__':
    main()
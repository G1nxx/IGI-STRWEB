from my_input import collection_for_serialization, randomize
from TASKS.TASK_1 import Executer as Executer_1
from TASKS.TASK_2 import Executer as Executer_2
from TASKS.TASK_2 import Printer
from TASKS.TASK_3 import Evaluator, Painter
from TASKS.TASK_4 import Executer as Executer_4
from TASKS.TASK_5 import Executer as Executer_5
from TASKS.TASK_6 import Executer as Executer_6
import getch

# Class is made to manage tasks
class task_manager:
    def __init__(self):
        pass

    # Task 1. Main goal is to serialize and deserialize data.
    def task1(self):
        school_workload = collection_for_serialization()
        columns = ["name", "load"]
        file_name = "loads"

        executer = Executer_1()
        executer.serialize(columns, file_name, _list=school_workload)

        new_workload = executer.deserealize(file_name)
        if new_workload is None:
            return
        
        executer.search(new_workload)
        executer.sort(new_workload)
        

    # Task 2. Main goal is to parse text and make file with information about it
    def task2(self):
        result_file_name = "result.txt"
        file_name = "mac.txt"
        executer = Executer_2()
        printer = Printer(result_file_name)
        text = executer.read_from_file(file_name)

        counters = executer.count_sentences(text)
        average_len_sentence = executer.average_len_of_sentence(text)
        average_len_word = executer.average_len_of_word(text)
        len_words = executer.count_words_in_sentences(text)
        longest_word = executer.find_longest_word(text)

        printer.print_about_setences(counters, average_len_sentence, average_len_word, len_words)
        printer.print_lowercase_words_and_punctuation(text)
        printer.print_all_macs(text)
        printer.print_longest_word(longest_word)
        printer.print_every_even_word(text)
        printer.print_all_emojis(text)
        printer.save_changes()

        executer.archivise(result_file_name)
        printer.print_info_about_zip()

        

    # Task 3. Main goal is to work with collections and make graphs
    def task3(self):
        collection = randomize(10) + [2, 2, 2, 2, 7]
        evaluator = Evaluator()
        painter = Painter()
        ar_mean = evaluator.arithmetic_mean(collection)
        median = evaluator.find_median(collection)
        moda = evaluator.find_moda(collection)
        variance = evaluator.find_variance(collection)
        deviation = evaluator.find_deviation(collection)

        print("Colection: " + str(collection))
        print("Sorted colection: " + str(sorted(collection)))
        print("Arithmatic mean: " + str(ar_mean))
        print("Madian: " + str(median))
        print("Moda: " + str(moda[0]) + ", occurs " + str(moda[1]) + " times")
        print("Variance: " + str(variance))
        print("Deviation: " + str(deviation))

        painter.draw_plot()


    # Task 4. Main goal is to paint Triangle, inherited from abstract Figure class
    def task4(self):
        #tr = Triangle(3, 60, 60, "Ellow")
        #print(tr)
        #tr2 = eval(repr(tr))      # Realization of __repr__ 'magic' method
        #print(tr2)
        executer = Executer_4()
        try:
            tr = executer.create_triangle()
        except Exception:
            print("Can`t to create such triangle")
        else:
            print(tr)
            tr.draw()

    # Task 5. Main goal is to work with numpy
    def task5(self):
        executer = Executer_5()
        executer.execute(3,4)

    # Task 6. Demonstration of pandas
    def task6(self):
        executer = Executer_6()
        executer.print_enterence()
        print("To see demonstration of pandas. Series press any key")
        getch.getch()
        executer.series_demo()
        print("To see demonstration of pandas. DataFrame press any key")
        getch.getch()
        print()
        executer.print()
if __name__ == '__main__':
    raise Exception("You can`t use this file as executable one")
from my_input import collection_for_serialization
from TASKS.TASK_1 import Executer as Executer_1
from TASKS.TASK_2 import Executer as Executer_2
from TASKS.TASK_2 import Printer

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
        file_name = "mac.txt"
        executer = Executer_2()
        printer = Printer()
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



        

    # Task 3. Main goal is to
    def task3(self):
        pass

    # Task 4. Main goal is to p
    def task4(self):
        pass

    # Task 5. Main goal is to 
    def task5(self):
        pass

if __name__ == '__main__':
    raise Exception("You can`t use this file as executable one")
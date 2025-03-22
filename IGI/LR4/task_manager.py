from my_input import collection_for_serialization
from TASKS.TASK_1 import Executer

# Class is made to manage tasks
class task_manager:
    def __init__(self):
        pass

    # Task 1. Main goal is to serialize and deserialize data.
    def task1(self):
        school_workload = collection_for_serialization()
        columns = ["name", "load"]
        file_name = "loads"

        executer = Executer()
        executer.serialize(columns, file_name, _list=school_workload)

        new_workload = executer.deserealize(file_name)
        if new_workload is None:
            return
        
        executer.search(new_workload)
        executer.sort(new_workload)
        

    # Task 2. Main goal is to 
    def task2(self):
        pass

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
from my_input import *
import pickle
import csv

# This class is made for serealization data
class Serializer:
    def __init__(self):
        pass
    
    # Serealizes data in csv format
    def serialize_csv(self, dict, columns, file_name):
        with open(file_name, "w") as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            writer.writerows(dict)

    # Deserealizes data in csv format
    def load_csv(self, file_name):
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            return list(reader)         
       
    # Serealizes data in pickle format     
    def serialize_pickle(self, dict, file_name):
        with open(file_name, "wb") as file:
            pickle.dump(dict, file)

    # Deserealizes data in pickle format
    def load_pickle(self, file_name):
        with open(file_name, "rb") as file:
            return pickle.load(file)

# This class is made for executing different operations with data
class Executer:
    def __init__(self):
        self.sr = Serializer()

    # Is used to chose serializer
    def serialize(self, _columns, _file_name, _list):
        while True:
            print("Do you want to serialize csv<1>, pickle<2> or both of them<3>?")
            inp = input_int();
            if inp < 1 or inp > 3:
                print("Chose one of sugested options")
                continue
            if inp != 1:
                self.sr.serialize_pickle(_list, _file_name + ".pickle")
            if inp != 2:
                self.sr.serialize_csv(_list, _columns, _file_name + ".csv")
            break

    # Is used to chose deserializer
    def deserealize(self, _file_name):
        try:
            while True:
                print("Do you want to read from csv<1> or pickle<2>?")
                inp = input_int();
                if inp < 1 and inp > 2:
                    print("Chose one of sugested options")
                    continue
                if inp == 1:
                    new_workload = self.sr.load_csv(_file_name + ".csv")
                elif inp == 2:
                    new_workload = self.sr.load_pickle(_file_name + ".pickle")
                break
        except FileNotFoundError:
            print("File doesn`t exist")
            return None
        except Exception:
            print("Unknow error. Please, try again")
            return None
        return new_workload
    
    # Is used to chose search options
    def search(self, _list):
        while True:
            print("Do you want to find element in collection by name<1>, by load<2> or don`t you<3>?")
            inp = input_int();
            if inp < 1 and inp > 3:
                print("Chose one of sugested options")
                continue
            if inp == 1:
                name = input("Enter name: ")
                checker = True
                for el in _list:
                    if el["name"] == name:
                        print("Load is " + str(el["load"]))
                        checker = False
                if checker:
                    print("No such element")
            elif inp == 2:
                load = input("Enter load: ")
                for el in _list:
                    if el["load"] == load:
                        print("Name is " + str(el["name"]))
                        checker = False
                if checker:
                    print("No such element")
            break
    
    # Is used to chose sort options
    def sort(self, new_workload):
        while True:
            print("Do you want to sort collection by name<1>, by load<2> or don`t you<3>?")
            inp = input_int();
            if inp < 1 and inp > 3:
                print("Chose one of sugested options")
                continue
            sorted_c = None
            if inp == 1:
                sorted_c = sorted(new_workload, key=lambda d: d["name"])
            if inp == 2:
                sorted_c = sorted(new_workload, key=lambda d: int(d["load"]))
            if inp == 3:
                break
            for el in sorted_c:
                print(el)
            break
        

if __name__ == '__main__':
    raise Exception("You can`t use this file as executable one")
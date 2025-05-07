import numpy as np
from my_input import array_gen

# This class is made for matrix operations
class Matrix:
    def __init__(self, n: int, m: int):
        self._n = n
        self._m = m
        self._arr = np.random.randint(low=0, high=100, size=(n, m))

    # Sorts last line of array
    def sort(self):
        self._arr[-1].sort()
        return self._arr
    
    # NumPy median realization
    def median(self):
        return np.median(self._arr[-1])
    
    # My median realization
    def my_median(self):
        arr = np.sort(self._arr[-1]).copy().tolist()
        if self._m % 2 == 0:
            return ((arr[self._m // 2] + arr[self._m // 2 - 1]) / 2)
        else:
            return arr[self._m // 2]

    def __str__(self):
        return self._arr.__str__()
    
# Class for execution operations with matrix
class Executer:
    def __init__(self):
        self.array = None

    # Realization of task
    def execute(self, n, m):
        try:
            arr = Matrix(n, m)
            print(arr)
            print(arr.sort())
            print("NumPy median: " + str(arr.median()))
            print("My median: " + str(arr.my_median()))
        except:
            print("Something went wrong.")


if __name__ == '__main__':
    raise Exception("You can`t use this file as executable one")
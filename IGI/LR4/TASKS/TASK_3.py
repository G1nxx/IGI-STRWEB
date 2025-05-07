import math 
import matplotlib.pyplot as plt
import numpy as np

# This class is made for operations with collections
class Evaluator:
    def __int__(self):
        pass

    # Evaluates factorial.
    def my_factorial(self, n: int) -> int:         
        if type(n) is not int:
            raise Exception("Invalid Type.")
        if n == 0:
            return 1
        else:
            return n * self.my_factorial(n-1)

    # Uses Maclore series to evaluate exp(x) whith accuracy = eps.
    def macloren_exp(self, x: float, eps: float) -> float:  
        n = 0
        Fx = 0.0
        MATH_Fx = math.exp(x)
        while eps < math.fabs(MATH_Fx - Fx):
            Fx += ((x**n) / self.my_factorial(n))
            n += 1
        return Fx
    
    # Finds arithmetic mean
    def arithmetic_mean(self, collection: list[float]) -> float:
        sum = 0;
        for el in collection:
            sum += el
        return sum / len(collection)
    
    # Finds median of collection
    def find_median(self, collection: list[float]) -> float:
        col_len = len(collection)
        collection = sorted(collection)
        if col_len % 2 == 0:
            return (collection[col_len // 2] + collection[col_len // 2 + 1]) / 2
        else:
            return collection[col_len // 2]
        
    # Finds moda of collection
    def find_moda(self, collection: list[float]):
        counter = {}
        for el in collection:
            if counter.get(el) is None:
                counter[el] = 1
            else:
                counter[el] += 1
        max = (0,0)
        for key in counter.keys():
            if counter[key] > max[1]:
                max = (key, counter[key])
        return max
    
    # Finds variance of collection
    def find_variance(self, collection: list[float]):
        av_mean = self.arithmetic_mean(collection)
        variance = 0
        for el in collection:
            variance += (el - av_mean) ** 2
        return variance / (len(collection) - 1)
    
    # Finds deviation of collection
    def find_deviation(self, collection: list[float]):
        variance = self.find_variance(collection)
        return math.sqrt(variance)

# This class is made for painting plots
class Painter:
    def __init__(self):
        pass

    # This methon is used to draw plot of exp(x) by points
    def draw_plot(self):
        i = 0
        ev = Evaluator()
        exp_values = {}
        mac_values = {}
        while i < 2:
            exp_values[i] = math.exp(i)
            mac_values[i] = ev.macloren_exp(i, 0.1)
            i += 0.1

        _, ax = plt.subplots(figsize=(10, 6), layout='constrained')
        ax.plot(exp_values.keys(), exp_values.values(), marker='o', linestyle='-', color='b', label='exp(x)')
        ax.plot(mac_values.keys(), mac_values.values(), marker='o', linestyle='-', color='r', label='mac(x)')
        ax.set_xlabel('i')
        ax.set_ylabel('val(i)')
        ax.set_title('Graphs exp(x)')
        ax.legend()
        plt.savefig("plot.png")
        plt.show()



if __name__ == '__main__':
    raise Exception("You can`t use this file as executable one")
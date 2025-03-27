from abc import ABC, abstractmethod
import math
import random
import matplotlib.pyplot as plt
from my_input import input_float, input_color

# Tnis class is made for being parametr
class Color:
    def __init__(self, name):
        self.__name = name

    # Realization of parametr, getter
    @property
    def name(self):
        return self.__name
    
    # Setter
    @name.setter
    def name(self, value):
        self.__name = value
    
    # Deleter
    @name.deleter 
    def name(self):
        del self.__name


# Abstract class for Triangle inharitance
class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def draw(self):
        pass


# This class represents geometric figure such as triangle
class Triangle(Figure):
    def __init__(self, _side: float, _angle_1: float, _angle_2: float, _color : Color, _name: str):
        self.name = _name
        self.color = _color
        self.side_1  = float(_side)
        self.angle_1 = float(_angle_1)
        self.angle_2 = float(_angle_2)
        self.angle_3 = 180.0 - self.angle_1 - self.angle_2
        self.side_2 = math.sin(self.angle_1 / 180.0 * math.pi) / math.sin(self.angle_3 / 180.0 * math.pi) * self.side_1
        self.side_3 = math.sin(self.angle_2 / 180.0 * math.pi) / math.sin(self.angle_3 / 180.0 * math.pi) * self.side_1
        print(self.side_1)
        print(self.side_2)
        print(self.side_3)
        print(self.angle_1)
        print(self.angle_2)
        print(self.angle_3)

        if self.side_1 <= 0 or self.side_2 <= 0 or self.side_3 <= 0:
            raise Exception("Can`t to create such triangle")
        if self.angle_1 <= 0 or self.angle_2 <= 0 or self.angle_3 <= 0:
            raise Exception("Can`t to create such triangle")
        if self.side_1 >= self.side_2 + self.side_3:
            raise Exception("Can`t to create such triangle")
        if self.side_2 >= self.side_1 + self.side_3:
            raise Exception("Can`t to create such triangle")
        if self.side_3 >= self.side_2 + self.side_1:
            raise Exception("Can`t to create such triangle")


    def name(self):
        return self.name
    
    # Counts area of triangle
    def area(self) -> float:
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3))

    # Counts perimeter of triangle
    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3
    
    # Draws triangle
    def draw(self):
        x1, y1 = 0, 0
        x2, y2 = x1 + self.side_1, 0
        x3 = (x1 + self.side_3) * math.cos(self.angle_1 / 180.0 * math.pi)
        y3 = (x1 + self.side_3) * math.sin(self.angle_1 / 180.0 * math.pi)

        plt.plot(x1, y1, marker = 'o', markersize = 10)
        plt.plot(x2, y2, marker = 'o', markersize = 10)
        plt.plot(x3, y3, marker = 'o', markersize = 10)

        plt.plot( 
            (x1, x2, x3, x1),   
            (y1, y2, y3, y1), 
            color = self.color.name
        )

        plt.text(x1 - 0.9, y1, 'A')
        plt.text(x2 + 0.4, y2, 'B')
        plt.text(x3, y3 + 0.3, 'C')
        plt.axis('equal')
        plt.savefig("figure" + str(random.randint(0,1000)) + ".png")
        plt.title(self.name)
        plt.show()
        
    # 'magic' method for convertion into string
    def __str__(self):
        s = "(Figure: {} | Color: {} | Sides: {} | Angles: {} | Perimeter: {} | Area: {:0.5f})"
        sides = (self.side_1, self.side_2, self.side_3)
        angles = (self.angle_1, self.angle_2, self.angle_3)
        return s.format(self.name, self.color.name, sides, angles, self.perimeter(), self.area())
    
    # 'magic' method for eval func 
    def __repr__(self):
        return f"Triangle(_side={self.side_1!r}, _angle_1={self.angle_1!r}, _angle_2={self.angle_2!r}, _color={self.color!r})"
    
# This class is made for creating triangles
class Executer():
    def __init__(self):
        pass
    
    def create_triangle(self) -> Triangle:
        print("Enter side: ", end='')
        side = input_float()
        print("Enter first angle: ", end='')
        angle_1 = input_float()
        print("Enter second angle: ", end='')
        angle_2 = input_float()
        print("Enter color: ", end='')
        color = Color(input_color())
        name = input("Enter name of figure: ")
        return Triangle(side, angle_1, angle_2, color, name)


if __name__ == '__main__':
    raise Exception("You can`t use this file as executable one")
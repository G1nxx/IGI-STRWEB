import math 

#Evaluates factorial.
def My_factorial(n) -> int:         
    if type(n) is not int:
        raise Exception("Invalid Type.")
    if n == 0:
        return 1
    else :
        return n * My_factorial(n-1)

#Uses Maclore series to evaluate exp(x) whith accuracy = eps.
def Macloren_exp(x, eps) -> (int | float | float) :  
    if type(x) is not float:
        raise Exception("Invalid Type.") 
    if type(eps) is not float:
        raise Exception("Invalid Type.") 
    n = 0
    Fx = 0.0
    MATH_Fx = math.exp(x)
    while eps < math.fabs(MATH_Fx - Fx):
        Fx += ((x**n) / My_factorial(n))
        n += 1
    return (n,Fx,MATH_Fx)
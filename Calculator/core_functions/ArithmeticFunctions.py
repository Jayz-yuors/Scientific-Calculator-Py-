import math 
class ArithmeticFunction:
    def add(self,a,b):
        return (a + b)
    def subtract(self,a,b) :
        return (a - b)
    def multiply(self,a,b):
        return (a*b) 
    def divide(self,a,b):
        if b == 0:
            print("Error: Division by zero is not allowed.")
            return None
        return (a/b)
    def floor(self,a,b):
        return(a//b)
    def power(self,a,b):
        return (a ** b)
    def square (self,a):
        return( a ** 2)
    def sqroot(self,a):
        if a < 0:
            print("Error:Cannot calculate square root of negative number :")
            return None
        return (math.sqrt(a))
    def cube(self,a):
        return(a ** 3)
    def cuberoot(self,a):
        if a < 0:
            print("Error:Cannot calculate cube root of negative number :")
            return None
        return (a ** (1/3))
    def gcd(self,a,b):
        return math.gcd(a,b)
    def lcm(self,a,b):
        return (a * b) // math.gcd(a, b)
    def factorial(self,a):
        if a < 0:
            print("Error: Factorial of negative number is not defined.")
            return None
        if a == 0 or a == 1:
            return 1
        result = 1
        for i in range(2, a + 1):
            result *= i
        return result 
    def nthroot(self,a,n):
        if a < 0 and n % 2 == 0:
            print("Error: cannot calculate even root of negative Number")
            return None
        return a ** (a/n)
    def percent(self,a,b):
        if b == 0:
            print("Error: Division by zero is not allowed.")
            return None
        return (a / b) * 100
    def roundf(self,a):
        return round(a)
    
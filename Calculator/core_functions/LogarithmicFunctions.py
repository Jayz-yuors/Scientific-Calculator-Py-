import math
class LogarithmicFunction :
    def log_base10(self,x):
        if x <= 0 :
            print("Error:Logarithm of negative number is not possible.:")
            return None
        return math.log10(x)
    def log_natural(self,x):
        if x <= 0 :
            print("Error:Logarithm of negative number is not possible.:")
            return None
        return math.log(x)
    def log_base(self,x,base):
        if x <= 0 or base <= 0 or base == 1:
            print("Error: Logarithm of negative number or base 1 is not possible.")
            return None
        return math.log(x, base)
    def exp_base10(self,x):
        return 10 ** x
    def exp_natural(self,x):
        return math.exp(x)
    def exp_base(self, x, base):
        if base <=0 :
            print("ERROR: Base must be positive:")
            return None
        return base ** x
    



    
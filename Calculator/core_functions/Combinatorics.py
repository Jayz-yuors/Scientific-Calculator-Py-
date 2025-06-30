import math
import random
class Combinatorics:
    def nPr_function(self, n: int, r:int ) -> int:
        if n < 0 or r < 0 or r >n :
            print("Error: Invalid values for n and r. Ensure n >= 0, r >= 0, and r <= n.")
            return None
        return math.factorial(n) // math.factorial(n-r)
    def nCr_function(self, n: int, r:int ) -> int:
        if n < 0 or r < 0 or r >n :
            print("Error: Invalid values for n and r. Ensure n >= 0, r >= 0, and r <= n.")
            return None
        return math.factorial(n) // (math.factorial(r)* math.factorial(n-r))
    def generate_random_float(self, low=0.0, high=1.0):
        if low >=high :
            print("Error:Low must be less than high.")
            return None
        return random.uniform(low,high)
    def generate_random_int(self, start : int,end : int) -> int:
     if  start>=end  :
        print("Error:Start must be less than End.")
        return None
     return random.randint(start,end)
         
      



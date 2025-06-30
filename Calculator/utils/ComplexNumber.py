import math
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def complex_add(self, other):
        return (self.real + other.real, self.imaginary + other.imaginary)
    def complex_subtract(self,other):
         return (self.real - other.real, self.imaginary - other.imaginary)
    def complex_multiply(self,other):
        real = (self.real * other.real) - (self.imaginary * other.imaginary)
        imaginary = (self.real *other.imaginary) + (self.imaginary * other.real)
        return (real,imaginary)
    def complex_divide(self,other):
        den = (other.real ** 2 + other.imaginary ** 2)
        if den == 0 :
            print("Error:Divison by zero not possible")
            return None
        real = ((self.real *other.real) + (self.imaginary * other.imaginary)) / den
        imaginary = ((self.imaginary * other.real) - (self.real * other.imaginary)) /den
        return (real,imaginary)
    def complex_conjugate(self):
        return(self.real, -self.imaginary)
    def complex_magnitude(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)
    def complex_argument(self):
        if self.real == 0 and self.imaginary == 0 :
            print("Error : Argument of zero not defined")
            return None
        return math.atan2(self.imaginary,self.real)
    def complex_to_polar(self):
        r = self.complex_magnitude()
        theta = self.complex_argument()
        if theta is None :
            return None
        theta = math.degrees(theta)
        return (r,theta)
    @staticmethod
    def polar_to_complex(r,theta,unit):
        if unit == 'DEGREE' :
            theta = math.radians(theta)
        elif unit !='RADIAN':
            print("Error: Unit must be either degrees or radians.")
            return None
        real = r *math.cos(theta)
        imaginary = r * math.sin(theta)
        return ComplexNumber(real,imaginary)
    @staticmethod
    def get_complex_input(prompt=""):
        print(prompt)
        form = input("Choose form : 1.Rectangular or 2.Polar : ")
        if form == '1':
            real = float(input("Enter real part :"))
            imag = float (input("Enter imaginary part :"))
            return ComplexNumber(real,imag)
        elif form == '2':
            r = float(input("Enter magnitude (r): "))
            theta = float(input("Enter angle (theta): "))
            unit = input("Enter unit (DEGREE/RADIAN): ").strip().upper()
            return ComplexNumber.polar_to_complex(r, theta, unit)
        else :
            print("Invalid Choice ! Using 0i + 0j")
            return ComplexNumber(0,0)


    
    
    

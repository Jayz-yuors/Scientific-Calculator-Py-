from re import match
from core_functions.ArithmeticFunctions import ArithmeticFunction
from core_functions.Combinatorics import Combinatorics
from core_functions.Coordinate import Coordinates
from core_functions.TrigonometricFunctions import TrigonometricFunction
from core_functions.NumberConversion import NumberConversion
from core_functions.NumricalFunctions import NumericalFunction
from core_functions.LogarithmicFunctions import LogarithmicFunction
from apps.DistributionData import DistributionData
from apps.StatisticalData import StatisticalData
from apps.InequalitySolver import InequalitySolver
from apps.EquationSolver import EquationSolver
from data.constants import constants
from data.conversions import conversion
from utils.ComplexNumber import ComplexNumber
from utils.Matrices import MatriceCalculator
from utils.Vectors import VectorCalculator
print("\n CALCULATOR-DETAILS \n This calculator has 4 modes according to the requirements\n 1.Core_functions \n 2.Apps \n 3.Data \n 4.Utils")
print("Mode 1 -> (core_functions) \n 1.ArithmeticFunctions \n 2.Combinatorics \n 3.Coordinate \n 4.TrigonometricFunctions \n 5.NumberConversions \n 6.NumricalFunctions \n 7.LogarithmicFunctions")
print("Mode 2 ->(apps) \n 1.DistributionData \n 2.StatisticalData \n 3.InequalitySolver \n 4.EquationSolver")
print("Mode 3 -> (data) \n 1.Constants \n 2.Conversions")
print("Mode 4 ->(utils ) \n 1.Matrices \n 2.Vectors \n 3.ComplexNumber ")
print()
while(1):
    c = int(input("\n Enter your Choice(core_functions- mode)  -> 1 for core_functions \n 2 for apps \n 3 for data \n 4 for utils \n 5 for EXIT \n"))
    if c == 5 :
        print("Exiting Program:")
    elif c == 1 :
        a = input("\n Enter choice(core_functions): 1.ArithmeticFunctions \n 2.Combinatorics \n 3.Coordinate \n 4.TrigonometricFunctions \n 5.NumberConversions \n 6.NumricalFunctions \n 7.LogarithmicFunctions \n")
        match a :
            case '1':
                x = int(input("\n Options -> 1.Additon \n 2.Subtraction \n 3.Multiply \n 4.Divide \n 5.Floor Divison \n 6.Power( a raised to b) \n 7.Square of a Number\n 8.Square Root of a Number\n 9.Cube of a Number \n 10.Cuberoot of a Number \n 11. GCD of a Number \n 12.LCM of a Number \n 13.Factorial of a Number \n 14.nth root of a Number \n 15.Percentage \n 16. Round off \nEnter your Choice \n "))
                af = ArithmeticFunction()
                match x:
                    case 1:
                        a = int(input("Enter 1st Number "))
                        b = int(input("Enter 2nd Number "))
                        result = af.add(a,b)
                        print(f"Answer of Addition of {a} and {b}->")
                        print(result)
                    case 2:
                        a = int(input("Enter 1st Number "))
                        b = int(input("Enter 2nd Number "))
                        result = af.subtract(a,b)
                        print(f"Result of Subtraction {a} and {b} ->")
                        print(result)
                    case 3:
                        a = int(input("Enter 1st Number "))
                        b = int(input("Enter 2nd Number "))
                        result = af.multiply(a,b)
                        print(f"Result of Multiplication of {a} and {b}")
                        print(result)
                    case 4:
                        a = int(input("Enter 1st Number "))
                        b = int(input("Enter 2nd Number "))
                        result = af.divide(a,b)
                        print(f"Result of Division of {a} over {b}")
                        print(result)
                    case 5:
                        a = int(input("Enter 1st Number "))
                        b = int(input("Enter 2nd Number "))
                        result = af.floor(a,b)
                        print(f"Result of Floor division of {a}and {b}->")
                        print(result)
                    case 6:
                        a = int(input("Enter 1st Number "))
                        b = int(input("Enter 2nd Number "))
                        result = af.power(a,b)
                        print(f"Result of raising {a} to  {b}->")
                        print(result)
                    case 7:
                        a = int(input("Enter the  Number :"))
                        result = af.square(a)
                        print(f"Answer of square of {a}->")
                        print(result)
                    case 8:
                        a = int(input("Enter the  Number :"))
                        result = af.sqroot(a)
                        print(f"Answer of square-root of {a}->")
                        print(result)
                    case 9:
                        a = int(input("Enter the  Number :"))
                        result = af.cube(a)
                        print(f"Answer of CUBE of {a}->")
                        print(result)
                    case 10:
                        a = int(input("Enter the  Number :"))
                        result = af.cuberoot(a)
                        print(f"Answer of CUBEROOT of {a}->")
                        print(result)
                    case 11:
                        a = int(input("Enter 1st Number for GCD "))
                        b = int(input("Enter 2nd Number for GCD"))
                        print(f"Result of GCD of {a}and {b}->")
                        result = af.gcd(a,b)
                        print(result)
                    case 12:
                        a = int(input("Enter 1st Number for LCM "))
                        b = int(input("Enter 2nd Number for LCM"))
                        result = af.lcm(a,b)
                        print(f"Result of LCM of {a}and {b}->")
                        print(result)
                    case 13:
                        a = int(input("Enter the  Number :"))
                        result = af.factorial(a)
                        print(f"Result of Factorial of {a}")
                        print(result)
                    case 14:
                        a = int(input("Enter 1st Number "))
                        b = int(input("Enter 2nd Number "))
                        result = af.nthroot(a,b)
                        print(f"Result of nthroot of {a}and {b}->")
                        print(result)
                    case 15:
                        a = int(input("Enter 1st Number for Percentage calculation(Numerator)"))
                        b = int(input("Enter 2nd Number (DENOMINATOR)"))
                        result = af.percent(a,b)
                        print(f"Result of percentage calculation of {a} over {b}->")
                        print(result)
                    case 16:
                        a = int(input("Enter the Number "))
                        print(f"Round off of {a}")
                        result = af.roundf(a)
                        print(result)
                    case _:
                        print("Invalid choice ! Try Again")
            case '2':
                x = int(input(" \n 1.nPr calculation \n 2.nCr Calculation \n 3.Generate random float \n 4.Generate Random Integer\n Enter Choice: "))
                cm = Combinatorics()
                match x :
                    case 1 :
                        n = int(input("Enter value of n: "))
                        r = int(input("Enter value of r: "))
                        result = cm.nPr_function(n,r)
                        print(f"The nPr combination of {n} and {r} as n and r respectively is {result}")
                    case 2 :
                        n = int(input("Enter value of n: "))
                        r = int(input("Enter value of r: "))
                        result = cm.nCr_function(n,r)
                        print(f"The nCr combination of {n} and {r} as n and r respectively is {result}")
                    case 3:
                        result = cm.generate_random_float()
                        print(f"The random float value between 0.0 and 1.0 is {result}")
                    case 4 :
                        a = int(input("Enter 1st Number :"))
                        b = int(input("Enter 2nd Number "))
                        result = cm.generate_random_int(a,b)
                        print(f"The random number between {a} and {b} : {result}")
                    case _:
                        print("Invalid Choice ! Try Again ")
            case '3':
                x = int(input(" \n 1. Polar to Cartesion conversion \n 2.Cartesian to Polar Conversion \n Enter your choice \n"))
                co = Coordinates()
                match x :
                    case 1 :
                        min_deg = -360
                        max_deg = 360
                        try:
                            a = float(input("Enter value of theta in Degrees"))
                            if not (min_deg <= a <= max_deg):
                                print(f"Please enter a degree value between {min_deg} and {max_deg}")
                        except ValueError:
                            print("Invalid input:Please enter a Number Value")
                        r = float(input("Enter value of r : "))
                        result = co.polar_to_cartesian(r,a,'DEGREE')
                        print(f"The Cartesian Coordinates of r(Radial Distance):{r} with Angle(theta) :{a} are :{result}")
                    case 2 :
                        x = float(input("Enter X coordinate : "))
                        y = float(input("Enter Y coordinate : "))
                        result = co.cartesian_to_polar(x,y)
                        print(f"The Polar Coordinates of {x},{y} :{result} in format of r,theta")
                    case _:
                        print("Invalid Choice ! Try Again")
            case '4':
                x = int(input("\n 1.Sine of an angle \n 2.Cosine of an angle \n 3.Tangent of an angle \n 4.Cosecant of an angle \n 5. Secant of an angle \n 6.Cotangent of an angle \n 7.Inverse of Sine \n 8.Inverse of Cosine \n 9. Inverse of Tangent \n 10.Hyperbolic Sine value \n 11.Hyperbolic Cosine value \n 12.Hyperbolic Tangent Value \n 13.Inverse Hyperbolic Sine value \n 14.Inverse Hyperbolic Cosine value \n 15.Inverse Hyperbolic Tangent value "))
                tf = TrigonometricFunction()
                match x :
                    case 1 :
                        a = float(input("Enter an angle in degrees"))
                        result = tf.sine(a,'DEGREE')
                        print(f"Angle :{a},Sine of that Angle {result}")
                    case 2 :
                        a = float(input("Enter an angle in degrees"))
                        result = tf.cosine(a,'DEGREE')
                        print(f"Angle :{a},Cosine of that Angle {result}")
                    case 3 :
                        a = float(input("Enter an angle in degrees"))
                        result = tf.tangent(a,'DEGREE')
                        print(f"Angle :{a},Tangent of that Angle {result}")
                    case 4 :
                        a = float(input("Enter an angle in degrees"))
                        result = tf.cosecant(a,'DEGREE')
                        print(f"Angle :{a},Cosecant of that Angle {result}")
                    case 5 :
                        a = float(input("Enter an angle in degrees"))
                        result = tf.secant(a,'DEGREE')
                        print(f"Angle :{a},Secant of that Angle {result}")
                    case 6 :
                        a = float(input("Enter an angle in degrees"))
                        result = tf.cotangent(a,'DEGREE')
                        print(f"Angle :{a},Cotangent of that Angle {result}")
                    case 7 :
                        a = float(input("Enter an angle in degrees"))
                        result = tf.inverse_sine(a)
                        print(f"Angle :{a},Inverse of Sine of that Angle {result}")
                    case 8 :
                        a = float(input("Enter an angle in degrees"))
                        result = tf.inverse_cosine(a)
                        print(f"Angle :{a},Inverse of Cosine of that Angle {result}")
                    case 9 :
                        a = float(input("Enter an angle in degrees"))
                        result = tf.inverse_tangent(a)
                        print(f"Angle :{a},Inverse of Tangent of that Angle {result}")
                    case 10 :
                        a = float(input("Enter an angle in degrees"))
                        result = tf.sineh(a)
                        print(f"Angle :{a},Hyperbolic Sine of that Angle {result}")
                    case  11 :
                        a = float(input("Enter an angle in degrees"))
                        result = tf.cosineh(a)
                        print(f"Angle :{a},Hyperbolic Cosine of that Angle {result}")
                    case 12 :
                        a = float(input("Enter an angle in degrees"))
                        result = tf.tangenth(a)
                        print(f"Angle :{a},Hyperbolic Tangent of that Angle {result}")
                    case 13 :
                        a = float(input("Enter an angle in degrees"))
                        result = tf.asinh(a)
                        print(f"Angle :{a},Inverse Hyperbolic Sine of that Angle {result}")
                    case 14 :
                        a = float(input("Enter an angle in degrees"))
                        result = tf.acosh(a)
                        print(f"Angle :{a},Inverse Hyperbolic Cosine of that Angle {result}")
                    case 15 :
                        a = float(input("Enter an angle in degrees"))
                        result = tf.atanh(a)
                        print(f"Angle :{a},Inverse Hyperbolic Tangent of that Angle {result}")
                    case _:
                        print("Invalid Choice !Try again ")
            case '5':
                x = int(input("\n 1.Decimal to Binary\n 2.Binary to Decimal \n 3.Decimal to Octal \n 4.Octal to Decimal \n 5.Decimal to Hexadecimal \n 6.Hexadecimal to Decimal \n 7.BIT_AND Operation \n 8.BIT_OR Operation \n 9.BIT_XOR Operation \n 10.BIT_XNOR Operation \n 11.BIT_NOT Operation \n 12.LEFT_SHIFT Operation \n 13.RIGHT_SHIFT Operation\n Enter your choice :"))
                nc = NumberConversion()
                match x :
                    case 1 :
                        a = float(input("Enter an Decimal Number : "))
                        result = nc.decimal_to_bin(a,fd=10)
                        print(f"The Binary Number Conversion of {a}[Decimal Number] is : {result}")
                    case 2 :
                        a = str(input("Enter Binary Number for Conversion->Note that the Input should be in format of '0b' or '0B' "))
                        a = a.strip()
                        if not a.startswith(('0b','0B')) :
                            print("Error : Input for the Binary Number must be '0b' or '0B' : ")
                        result = nc.bin_to_decimal(a)
                        print(f"The Decimal Conversion of {a}[Binary-Number] is : {result}")
                    case 3 :
                        a = float(input("Enter an Decimal Number : "))
                        result = nc.decimal_to_octal(a,fd=10)
                        print(f"The Octal Number Conversion of {a}[Decimal Number] is : {result}")
                    case 4 :
                        a = str(input("Enter Octal Number for Conversion->Note that the Input should be in format of '0o' or '0O' "))
                        a = a.strip()
                        if not a.startswith(('0o','0O')) :
                            print("Error : Input for the Binary Number must be '0b' or '0B' : ")
                        result = nc.oct_to_decimal(a)
                        print(f"The Decimal Conversion of {a}[Octal- Number] is : {result}")
                    case 5 :
                        a = float(input("Enter an Decimal Number : "))
                        result = nc.decimal_to_hex(a,fd=10)
                        print(f"The Hexadecimal Number Conversion of {a}[Decimal Number] is : {result}")
                    case 6 :
                        a = str(input("Enter Hexadecimal Number for Conversion->Note that the Input should be in format of '0x' or '0X' "))
                        a = a.strip()
                        if not a.startswith(('0x','0X')) :
                            print("Error : Input for the Binary Number must be '0x' or '0X' : ")
                        result = nc.hex_to_decimal_to_decimal(a)
                        print(f"The Decimal Conversion of {a}[Octal- Number] is : {result}")
                    case 7 :
                        a = int(input("Enter first Number "))
                        b = int(input("Enter 2nd Number "))
                        result = nc.bit_and(a,b)
                        print(f"Result of BIT_AND Operation(BINARY FORMAT) of {a} and {b}: {result}")
                    case 8 :
                        a = int(input("Enter first Number "))
                        b = int(input("Enter 2nd Number "))
                        result = nc.bit_or(a,b)
                        print(f"Result of BIT_OR Operation(BINARY FORMAT) of {a} and {b}: {result}")
                    case 9 :
                        a = int(input("Enter first Number "))
                        b = int(input("Enter 2nd Number "))
                        result = nc.bit_xor(a,b)
                        print(f"Result of BIT_XOR Operation(BINARY FORMAT) of {a} and {b}: {result}")
                    case 10 :
                        a = int(input("Enter first Number "))
                        b = int(input("Enter 2nd Number "))
                        result = nc.bit_xnor(a,b)
                        print(f"Result of BIT_XNOR Operation(BINARY FORMAT) of {a} and {b}: {result}")
                    case 11 :
                        a = int(input("Enter first Number "))
                        b = int(input("Enter 2nd Number "))
                        result = nc.bit_not(a,b)
                        print(f"Result of BIT_NOT Operation(BINARY FORMAT) of {a} and {b}: {result}")
                    case 12 :
                        a = float(input("Enter the Number "))
                        b = float(input("Enter Shift (by how many places ): "))
                        result = nc.bit_left_shift(a,b)
                        print(f"Result of BIT_LEFT_SHIFT of {a} by {b} SHIFTS : {result}")
                    case 13 :
                        a = float(input("Enter the Number "))
                        b = float(input("Enter Shift (by how many places ): "))
                        result = nc.bit_right_shift(a,b)
                        print(f"Result of BIT_LEFT_SHIFT of {a} by {b} SHIFTS : {result}")
                    case _:
                        print("Invalid Choice ! Try Again")
            case '6':
                x =int(input("\n 1.Differentiation \n 2.Integration \n Enter choice :"))
                nf = NumericalFunction()
                print("a)Enter expression  \n b) If power is present , it should be x ** n (n= power value) if x is used as variable,simultaneously for complex expression , Follow Expression format , eg sin(x) , log(x) , tanh(x) etc \n c) Expression variable and variable with which Operation is conducted should be SAME ")
                match x :
                    case 1 :
                        x = input("Enter Expression : ")
                        y = input("Enter variable with which differentiation will occur :")
                        a = float(input("Enter value at which differentiation answer should come "))
                        result = nf.Differentiation(x,y,a)
                        print(f"The Value of the expression {x} after Differentiation is : {result}")
                    case 2 :
                        x = input("Enter Expression : ")
                        y = input("Enter variable with which integration will occur :")
                        a = float(input("Enter value at which integrated answer should come "))
                        result = nf.Integration(x,y,a)
                        print(f"The Value of the expression {x} after Differentiation is : {result}")
                    case _:
                        print("Invalid Choice ! Try Again ")
            case '7':
                x =int(input("\n 1.Log to the Base 10 \n 2.Natural Logarithm \n 3.Logarithm with User Input (Base) \n 4. Exponential(base = 10) \n 5. Exponential(base = e) \n 6.Exponential(base = User Input) \n Enter your choice :"))
                lf = LogarithmicFunction()
                match x :
                    case 1 :
                        x = float(input("Enter Number :"))
                        result = lf.log_base10(x)
                        print(f"Logarithm of {x} to the base 10 is :{result}")
                    case 2 :
                        x = float(input("Enter Number :"))
                        result = lf.log_natural(x)
                        print(f"Logarithm of {x} to the Natural Base is :{result}")
                    case 3 :
                        x = float(input("Enter the Number :"))
                        y = float(input("Enter Base :"))
                        result = lf.log_base(x,y)
                        print(f"Logarithm of {x} to the Base {y} is :{result}")
                    case 4 :
                        x = float(input("Enter Number :"))
                        result = lf.exp_base10(x)
                        print(f" 10 raised to {x} :{result} ")
                    case 5 :
                        x = float(input("Enter Number :"))
                        result = lf.exp_natural(x)
                        print(f" e raised to {x} :{result} ")
                    case 6 :
                        x = float(input("Enter Number :"))
                        y = float(input("Enter Base : "))
                        result = lf.exp_base(x,y)
                        print(f" {y} raised to {x} :{result} ")
                    case _:
                        print("Invalid Input ! Try Again ")
            case _:
                print("Error : Invalid Choice Try Again")
    elif c == 2:
        a = input("\n Enter your choice(apps-mode) -> 1.DistributionData \n 2.StatisticalData \n 3.Inequality Solver \n 4.Equation Solver \n Enter your choice : ")
        match a :
            case '1':
                print("\n PDF -> Probability Distribution Function \n 2.CDF -> Cumulative Distribution Function")
                x = int(input("1.Normal PDF \n 2.Normal CDF \n 3.Inverse Normal CDF \n 4.Binomial PDF \n 5. Binomial CDF \n 6.Poisson PDF \n 7.Poisson CDF \n Enter your choice : "))
                dd = DistributionData()
                match x :
                    case 1:
                        xval = float(input("Enter X value :"))
                        mean = float(input("Enter Mean (μ)"))
                        stdev = float(input("Enter Standard Deviation (σ):"))
                        result = dd.normal_pdf(xval,mean,stdev)
                        print(f"NORMAL PDF at x ={xval} with MEAN :{mean} and STDEV as {stdev} is :{result}")
                    case 2 :
                        xval = float(input("Enter X value :"))
                        mean = float(input("Enter Mean (μ)  :"))
                        stdev = float(input("Enter Standard Deviation (σ):"))
                        result = dd.normal_cdf(xval,mean,stdev)
                        print(f"NORMAL CDF at x ={xval} with MEAN :{mean} and STDEV as {stdev} is :{result}")
                    case 3 :
                        prob = float(input("Enter Probability(0-1):"))
                        mean = float(input("Enter mean (μ):"))
                        stdev = float(input("Enter standard deviation (σ): "))
                        result = dd.inverse_normal_cdf(prob, mean, stdev)
                        print(f"Inverse CDF for p :{prob} for mean :{mean} and stdev:{stdev} is : {result}")
                    case 4 :
                        k = int(input("Enter number of successes (k): "))
                        n = int(input("Enter number of trials (n): "))
                        p = float(input("Enter success probability (p): "))
                        result = dd.binomial_pdf(k, n, p)
                        print(f"Binomial PMF: P(X={k}) = {result:.6f}")
                    case 5 :
                        k = int(input("Enter max successes (k): "))
                        n = int(input("Enter number of trials (n): "))
                        p = float(input("Enter success probability (p): "))
                        result = dd.binomial_cdf(k, n, p)
                        print(f"Binomial CDF: P(X≤{k}) = {result:.6f}")
                    case 6:  # Poisson PDF
                        k = int(input("Enter number of events (k): "))
                        lambda_val = float(input("Enter rate (λ): "))
                        result = dd.poisson_pdf(k, lambda_val)
                        print(f"Poisson PMF: P(X={k}) = {result:.6f}")
                    case 7:  # Poisson CDF
                        k = int(input("Enter max events (k): "))
                        lambda_val = float(input("Enter rate (λ): "))
                        result = dd.poisson_cdf(k, lambda_val)
                        print(f"Poisson CDF: P(X≤{k}) = {result:.6f}")
                    case _:
                        print("Invalid  choice !Try Again ")
            case '2':
                x = int(input("\n 1. For One Variable Data \n 2. For 2 Variable Data \n Enter your choice : "))
                sd = StatisticalData()
                match x :
                    case 1 :
                        x = int(input("1.Returning Data\n 2.Mean of Data \n 3.Sum of Data \n 4.Squared Sum of Data  \n 5.GET stdev_POPULATION \n 6. GET stdev.SAMPLE \n 7.Count(length of data ) \n 8.Get Least among data \n 9.Get Highest among Data \n 10.Get Median of Data \n 11.Get Quartiles of Data\n 12.ALL FUNCTIONS \n Enter your choice : "))
                        match x :
                            case 1 :
                                a = input("Enter Numbers seperated by one space -> ' ' ")
                                list = [float(x)for x in a.split()]
                                result = sd.one_vardata(list)
                                print(f"List of DATA:{result}")
                            case 2 :
                                a = input("Enter Numbers seperated by one space -> ' ' ")
                                list = [float(x)for x in a.split()]
                                result = sd.get_mean(list)
                                print(f"List:{list}\nMean of the Data Elements :{result}")
                            case 3 :
                                a = input("Enter Numbers seperated by one space -> ' ' ")
                                list = [float(x)for x in a.split()]
                                result = sd.get_sum(list)
                                print(f"List:{list}\nSum of Data Elements:{result}")
                            case 4 :
                                a = input("Enter Numbers seperated by one space -> ' ' ")
                                list = [float(x)for x in a.split()]
                                result = sd.get_sum_squared(list)
                                print(f"List:{list}\nSQUARED SUM of Data elements :{result}")
                            case 5:
                                a = input("Enter Numbers seperated by one space -> ' ' ")
                                list = [float(x)for x in a.split()]
                                result = sd.get_stdev_population(list)
                                print(f"List:{list}\nSTDEV_POPULATION:{result}")
                            case 6 :
                                a = input("Enter Numbers seperated by one space -> ' ' ")
                                list = [float(x)for x in a.split()]
                                result = sd.get_sample(list)
                                print(f"List:{list}\nSTDEV_SAMPLE:{result}")
                            case 7 :
                                a = input("Enter Numbers seperated by one space -> ' ' ")
                                list = [float(x)for x in a.split()]
                                result = sd.get_count(list)
                                print(f"List:{list}\nCOUNT:{result}")
                            case 8 :
                                a = input("Enter Numbers seperated by one space -> ' ' ")
                                list = [float(x)for x in a.split()]
                                result = sd.get_min(list)
                                print(f"List:{list}\nLeast among the DATA list :{result}")
                            case 9 :
                                a = input("Enter Numbers seperated by one space -> ' ' ")
                                list = [float(x)for x in a.split()]
                                result = sd.get_max(list)
                                print(f"List:{list}\nMax among the Data List:{result}")
                            case 10 :
                                a = input("Enter Numbers seperated by one space -> ' ' ")
                                list = [float(x)for x in a.split()]
                                result = sd.get_median(list)
                                print(f"List:{list}\nMEDIAN:{result}")
                            case 11 :
                                a = input("Enter Numbers seperated by one space -> ' ' ")
                                list = [float(x)for x in a.split()]
                                result = sd.get_quartiles(list)
                                print(f"List:{list}\nMean:{result}")
                            case 12 :
                                a = input("Enter Numbers seperated by one space -> ' ' ")
                                list = [float(x)for x in a.split()]
                                result = sd.all_functions(list)
                                print(f"List:{list}\n ALL INFO\n :{result}")
                            case _:
                                print("Invalid Choice ! Try again")
                    case 2 :
                        x = int(input("1.Returning Data for Both Lists \n 2.Get Mean of X List & Get mean of Y list \n 3.Get SUM of List X & Get SUM of List Y \n 4.Get SQUARED-SUM of List X & Get SQUARED-SUM of List Y \n 5.Get stdev_Population of List X & Get stdev_Population of List Y \n 6.Get stdev_sample of List X & Get stdev_sample of List Y \n 7. Get combined sum of List X and List Y \n 8.Linear Regression \n 9.Quadratic Regression\n Enter your choice :"))
                        match x :
                            case 1 :
                                a = input("Enter Numbers seperated by one space(List X) -> ' '")
                                Xlist = [float(x)for x in a.split()]
                                b = input("Enter Numbers seperated by one space(List Y)-> ' ' ")
                                Ylist = [float(x)for x in b.split()]
                                result = sd.two_vardata(Xlist,Ylist)
                                print(f"Both List are as follows \n List X :{Xlist}\n List Y :{Ylist}")
                            case 2 :
                                a = input("Enter Numbers seperated by one space(List X) -> ' '")
                                Xlist = [float(x)for x in a.split()]
                                result = sd.get_mean_x(Xlist)
                                print(f"Mean of XList : {result}")
                                b = input("Enter Numbers seperated by one space(List X) -> ' '")
                                Ylist = [float(x)for x in b.split()]
                                result = sd.get_mean_x(Ylist)
                                print(f"Mean of YList : {result}")
                            case 3 :
                                a = input("Enter Numbers seperated by one space(List X) -> ' '")
                                Xlist = [float(x)for x in a.split()]
                                result = sd.get_sum_x(Xlist)
                                print(f"Sum of XList : {result}")
                                b = input("Enter Numbers seperated by one space(List X) -> ' '")
                                Ylist = [float(x)for x in b.split()]
                                result = sd.get_mean_x(Ylist)
                                print(f"Sum of Ylist : {result}")
                            case 4 :
                                a = input("Enter Numbers seperated by one space(List X) -> ' '")
                                Xlist = [float(x)for x in a.split()]
                                result = sd._get_sum_x_squared(Xlist)
                                print(f"SQUARED-SUM of XList : {result}")
                                b = input("Enter Numbers seperated by one space(List X) -> ' '")
                                Xlist = [float(x)for x in b.split()]
                                result = sd._get_sum_y_squared(Ylist)
                                print(f"SQUARED-SUM of YList : {result}")
                            case 5 :
                                a = input("Enter Numbers seperated by one space(List X) -> ' '")
                                Xlist = [float(x)for x in a.split()]
                                result = sd._get_stdev_population_x(Xlist)
                                print(f"STDEV-POPULATION of XList : {result}")
                                b = input("Enter Numbers seperated by one space(List X) -> ' '")
                                Ylist = [float(x)for x in b.split()]
                                result = sd._get_stdev_population_y(Xlist)
                                print(f"STDEV-POPULATION of YList : {result}")
                            case 6 :
                                a = input("Enter Numbers seperated by one space(List X) -> ' '")
                                Xlist = [float(x)for x in a.split()]
                                result = sd._get_stdev_sample_x(Xlist)
                                print(f"STDEV-SAMPLE of XList : {result}")
                                b = input("Enter Numbers seperated by one space(List X) -> ' '")
                                Ylist = [float(x)for x in b.split()]
                                result = sd._get_stdev_sample_y(Ylist)
                                print(f"STDEV-SAMPLE of YList : {result}")
                            case 7 :
                                a = input("Enter Numbers seperated by one space(List X) -> ' '")
                                Xlist = [float(x)for x in a.split()]
                                b = input("Enter Numbers seperated by one space(List Y)-> ' ' ")
                                Ylist = [float(x)for x in b.split()]
                                result = sd.get_sum_xy(Xlist,Ylist)
                                print(f"Combined Sum of Elements of Xlist and Ylist respectively is :{result}")
                            case 8:
                                a = input("Enter Numbers seperated by one space(List X) -> ' '")
                                Xlist = [float(x)for x in a.split()]
                                b = input("Enter Numbers seperated by one space(List Y)-> ' ' ")
                                Ylist = [float(x)for x in b.split()]
                                result = sd.perform_linear_regression(Xlist,Ylist)
                                print(f"Linear Regression of XList and YList is :{result}")
                            case 9 :
                                a = input("Enter Numbers seperated by one space(List X) -> ' '")
                                Xlist = [float(x)for x in a.split()]
                                b = input("Enter Numbers seperated by one space(List Y)-> ' ' ")
                                Ylist = [float(x)for x in b.split()]
                                result = sd.perform_quadratic_regression(Xlist,Ylist)
                                print(f"Quadratic Regression of XList and YList is :{result}")
                            case _:
                                print("Invalid Choice ! Try Again")
            case '3':
                x = int(input("\n 1.Solve Polynomial Inequality : \n Enter your choice"))
                pi = InequalitySolver()
                match x :
                    case 1 :
                        print("Enter coefficients of the Polynomial Equation(From Higher Degree to Lower Degree) \n For eg -> x ** 2 - 3*x + 2 -> [1,-3,2]\n")
                        x = (input("\nEnter inputs for Coefficients seperated by one space -> ' ' :"))
                        Xlist = [float(a)for a in x.split()]
                        y = input("Enter variable eg x,y etc :")
                        s = int(input("Enter Operator Serial No -> 1.'>' \n 2.'<' \n 3.'>=' \n 4.'<=' \n Enter your choice : "))
                        match s :
                            case 1 :
                                result = pi.solve_PolynomialInequality(Xlist,'>',y)
                                print(f"Result : \n {result}")
                            case 2 :
                                result = pi.solve_PolynomialInequality(Xlist,'<',y)
                                print(f"Result : \n {result}")
                            case 3 :
                                result = pi.solve_PolynomialInequality(Xlist,'>=',y)
                                print(f"Result : \n {result}")
                            case 4 :
                                result = pi.solve_PolynomialInequality(Xlist,'<=',y)
                                print(f"Result : \n {result}")
                            case _:
                                print("Invalid Choice ! Try Again")
                    case _:
                        print("Invalid Choice ! Try again")
            case '4':
                x = int(input("\n 1.Solve Simultaneous Equations \n 2.Solve Polynomial Equations \n 3.Sovle Single Variable Equation \n Enter your Choice : "))
                es  = EquationSolver()
                match x :
                    case 1 :
                        n = int(input("\n Enter number of equations/variables :"))
                        coeffMatrix = []
                        for i in range (n):
                            row = input(f"Enter coefficients for equation {i+1} seperated by one space -> ' ' : ")
                            coeff = [float(x) for x in row.split()]
                            if len(coeff) !=n :
                                print(f"Error: Equation {i+1} must have exactly {n} coefficients.")
                            coeffMatrix.append(coeff)
                        else :
                            x = input("Enter Constants Vector seperated by one space -> ' ' :")
                            constants = [float(a) for a in x.split()]
                            if len(constants) != n:
                               print(f"Error: Constants vector must have exactly {n} values.")
                            else:
                              result = es.solve_SimultaneousEquation(coeffMatrix, constants)
                              print("Solution:", result)
                    case 2 :
                        print("Enter Coefficients of Higher Degree first ! \n for eg x**3 - 3*x**2 + 2 -> [1 -3 0 0 2]")
                        x = input("Enter Polynomial Coefficients seperated by one space -> ' ' : ")
                        coeff = [float(a) for a in x.split()]
                        result = es.solve_PolynomialEquation(coeff)
                        print(f"Roots : \n {result}")
                    case 3 :
                        equation = input("Enter equation (e.g., 'x**2 - 3*x + 2'): ")
                        variable = input("Enter variable name: ")
                        initial_guess = float(input("Enter initial guess: "))
                        result = es.solve_SingleVariableEquation(equation, variable, initial_guess)
                        print("Solution:", result)
                    case _:
                        print("Invalid Choice !Try Again")
            case _:
                print("Invalid Choice !Try again")
    elif c == 3 :
        a = (input("Enter your Choice(data-mode) -> \n 1.Constants \n 2.Conversions \n Enter your choice : "))
        match a :
            case '1':
                x = int(input("\n 1.Speed of light (m/s)\n 2. Gravitational constant (N m^2 / kg^2)\n 3. Planck constant (J s) \n 4. Avogadro constant (1/mol) \n 5. Boltzmann constant (J/K) \n 6. Molar gas constant (J/(mol·K)) \n 7. Permeability of vacuum (N/A^2) \n 8. Permittivity of vacuum (F/m) \n 9.Electron mass (kg) \n 10.Proton mass (kg) \n 11.Neutron mass (kg) \n 12.Value of PI \n 13.Value of E(exponential) \n Enter your choice : "))
                cc = constants()
                match x :
                    case 1 :
                        result = cc.get_scientific_constant('C')
                        print(f"Speed of Light :{result} m/s")
                    case 2 :
                        result = cc.get_scientific_constant('G')
                        print(f"Gravitational Constant :{result} N m^2 / kg^2")
                    case 3 :
                        result = cc.get_scientific_constant('H')
                        print(f" Planck's Constant :{result} J/s ")
                    case 4 :
                        result = cc.get_scientific_constant('NA')
                        print(f"Avogadro's Constant  :{result} 1/mol ")
                    case 5 :
                        result = cc.get_scientific_constant('K')
                        print(f"Boltzmann Constant :{result} J/K")
                    case 6 :
                        result = cc.get_scientific_constant('R')
                        print(f"Molar Gas Constant :{result} J/mol·K")
                    case 7 :
                        result = cc.get_scientific_constant('MU0')
                        print(f"Permeability of Vaccum  :{result} N/A^2")
                    case 8 :
                        result = cc.get_scientific_constant('EPS0')
                        print(f"Permittivity of Vaccum  :{result} N/A^2")
                    case 9 :
                        result = cc.get_scientific_constant('ME')
                        print(f"Electron Mass :{result} kg")
                    case 10 :
                        result = cc.get_scientific_constant('MP')
                        print(f"Proton Mass :{result} kg")
                    case 11 :
                        result = cc.get_scientific_constant('MN')
                        print(f"Neutron Mass :{result} kg")
                    case 12 :
                        result = cc.get_scientific_constant('PI')
                        print(f"Value of PI :{result} units")
                    case 13 :
                        result = cc.get_scientific_constant('E')
                        print(f"Value of exponential  :{result} units")
                    case _:
                        print("\n Invalid Choice ! Try Again")
            case '2':
                categories = {
                             1: ("LENGTH", list(conversion.UNIT_FACTORS["LENGTH"].keys())),
                             2: ("MASS", list(conversion.UNIT_FACTORS["MASS"].keys())),
                             3: ("TIME", list(conversion.UNIT_FACTORS["TIME"].keys())),
                             4: ("TEMPERATURE", list(conversion.TEMPERATURE_FUNCS.keys()))
                            }
                print("\nUnit Conversion Categories:")
                print("1. Length")
                print("2. Mass")
                print("3. Time")
                print("4. Temperature")
                cat_choice = int(input("Enter the category number: "))
                if cat_choice not in categories:
                    print("Invalid category choice.")
                else :
                    cat_name,units = categories[cat_choice]
                    print(f"\nAvailable units for {cat_name}:")
                    print(",".join(units))
                    from_unit = input("Enter the FROM unit: ").strip().upper()
                    to_unit = input("Enter the TO unit: ").strip().upper()
                    if from_unit not in units:
                       print(f"Error: {from_unit} is not a valid {cat_name} unit.")
                    elif to_unit not in units :
                        print(f"Error :{to_unit} is not a valid {cat_name} unit.")
                    else :
                        try :
                            value = float(input("Enter the value to convert: "))
                            result = conversion.convert_unit(value,from_unit,to_unit)
                            print(f"{value} {from_unit} = {result} {to_unit}")
                        except Exception as e :
                            print (e)
            case _:
                print("Invalid choice ! Try again :")   
    elif c == 4 :
        a = input("\n Enter your  choice (utils mode ->) : \n1.Complex Number \n 2.Matrices \n 3.Vectors \n Enter your choice :") 
        match a:
            case '1' :
                print("\nComplex Number Operations:")
                print("1. Add")
                print("2. Subtract")
                print("3. Multiply")
                print("4. Divide")
                print("5. Conjugate")
                print("6. Magnitude")
                print("7. Argument (radians)")
                print("8. Convert to Polar")
                print("RECTANGULAR FORM -> (a+bi) \n POLAR FORM -> (r,theta)")
                choice = int(input("Enter Operation Choice:"))
                if choice  in [1,2,3,4]:
                    c1 = ComplexNumber.get_complex_input("First complex Number :")
                    c2 = ComplexNumber.get_complex_input("Second Complex Number : ")
                    if choice == 1 :
                        result = c1.complex_add(c2)
                        print(f"Result of Addition : {result[0]} + {result[1]}i")
                    elif choice == 2 :
                        result = c1.complex_subtract(c2)
                        print(f"Result of Subtraction : {result[0]} + {result[1]}i")
                    elif choice == 3:
                        result = c1.complex_multiply(c2)
                        print(f"Result of Multiplication: {result[0]} + {result[1]}i")
                    elif choice == 4 :
                        result = c1.complex_divide(c2)
                        print(f"Result of Division : {result[0]} + {result[1]}i") if result else print("Divison Failed")
                elif choice in [ 5,6,7,8]:
                    c = ComplexNumber.get_complex_input("Enter Complex Number :")
                    if choice  == 5 :
                        result = c.complex_conjugate()
                        print(f"Conjugate: {result[0]} + {result[1]}i")
                    elif choice == 6:  # Magnitude
                        result = c.complex_magnitude()
                        print(f"Magnitude: {result}")
                    elif choice == 7 :
                        result = c.complex_argument()
                        print(f"Arugument: {result} radians")
                    elif choice == 8 :
                        r, theta_deg = c.complex_to_polar()
                        print(f"Polar form: r = {r}, θ = {theta_deg}°")
                    else:
                        print("Invalid operation choice")
            case '2':
                x = int(input("1.ADD 2 Matrices \n 2.ADD 3 Matrices \n 3. Matrix-Subtraction \n 4.Matrix-Multiplication \n 5.Matrix-Scalar Multiplication \n 6.Matrix-Determinant \n 7.Matrix-Inverse \n 8.Matrix-Transpose \n 9.Rank of a Matrix \n 10.Eigen Values of a Matrix \n 11.Eigen Vectors and Eigen Values of a Matrix \n 12.Augmented Matrix(A|B) \nEnter your choice :"))  
                mo =MatriceCalculator()
                match x :
                    case 1 :
                        mat1 = MatriceCalculator.get_matrix_input("Enter 1st Matrix :")
                        if mat1 is None :
                            break
                        mat2 = MatriceCalculator.get_matrix_input("Enter 2nd Matrix: ")
                        if mat2 is None :
                            break
                        result = mo.MatriceAdd(mat1,mat2)
                        if isinstance(result,list):
                            print("Addition of 2 Matrices -> ")
                            MatriceCalculator.print_matrix(result)
                    case 2 :
                        mat1 = MatriceCalculator.get_matrix_input("Enter 1st Matrix :")
                        if mat1 is None :
                            break
                        mat2 = MatriceCalculator.get_matrix_input("Enter 2nd Matrix: ")
                        if mat2 is None :
                            break
                        mat3 = MatriceCalculator.get_matrix_input("Enter 3rd Matrix: ")
                        if mat3 is None :
                            break
                        result = mo.MatriceAdd_3(mat1,mat2,mat3)
                        if isinstance(result,list):
                            print("Addition of 3 Matrices -> ")
                            MatriceCalculator.print_matrix(result)
                    case 3 :
                        mat1 = MatriceCalculator.get_matrix_input("Enter 1st Matrix :")
                        if mat1 is None :
                            break
                        mat2 = MatriceCalculator.get_matrix_input("Enter 2nd Matrix: ")
                        if mat2 is None :
                            break
                        result = mo.MatriceSub(mat1,mat2)
                        if isinstance(result,list):
                            print("Subtraction of 2 Matrices -> ")
                            MatriceCalculator.print_matrix(result)
                    case 4 :
                        mat1 = MatriceCalculator.get_matrix_input("Enter 1st Matrix :")
                        if mat1 is None :
                            break
                        mat2 = MatriceCalculator.get_matrix_input("Enter 2nd Matrix: ")
                        if mat2 is None :
                            break
                        result = mo.MatricesMul(mat1,mat2)
                        if isinstance(result,list):
                            print("Multiplication of 2 Matrices -> ")
                            MatriceCalculator.print_matrix(result)
                    case 5 :
                        mat1 = MatriceCalculator.get_matrix_input("Enter 1st Matrix :")
                        if mat1 is None :
                            break
                        s = float(input("Enter an Scalar Value :"))
                        result = mo.Matrice_scalarMul(mat1,s)
                        if isinstance(result,list):
                            print("Scalar Multiplication Result :  -> ")
                            MatriceCalculator.print_matrix(result)
                    case 6 :
                        mat1 = MatriceCalculator.get_matrix_input("Enter 1st Matrix :")
                        if mat1 is None :
                            break
                        result = mo.MatriceDeterminant(mat1)
                        print(f"Matrix Determinant Result :  -> {result}")
                    case 7 :
                        mat1 = MatriceCalculator.get_matrix_input("Enter 1st Matrix :")
                        if mat1 is None :
                            break
                        result = mo.MatriceInverse(mat1)
                        if isinstance(result,list):
                            print("Inverse of the Matrice  -> ")
                            MatriceCalculator.print_matrix(result)
                    case 8 :
                        mat1 = MatriceCalculator.get_matrix_input("Enter 1st Matrix :")
                        if mat1 is None :
                            break
                        result = mo.MatriceTranspose(mat1)
                        if isinstance(result,list):
                            print("Transpose of the Matrice  -> ")
                            MatriceCalculator.print_matrix(result)
                    case 9 :
                        mat1 = MatriceCalculator.get_matrix_input("Enter 1st Matrix :")
                        if mat1 is None :
                            break
                        result = mo.MatriceRank(mat1)
                        print(f"Rank of the Matrice  ->{result} ")
                    case 10 :
                        mat1 = MatriceCalculator.get_matrix_input("Enter 1st Matrix :")
                        if mat1 is None :
                            break
                        result = mo.MatriceEigenValues(mat1)
                        print(f"Eigen values of the Matrice  ->{result} ")
                    case 11 :
                        mat1 = MatriceCalculator.get_matrix_input("Enter 1st Matrix :")
                        if mat1 is None :
                            break
                        result = mo.MatriceEigenVectors(mat1)
                        if isinstance(result, tuple):
                            eigenvalues, eigenvectors = result
                        print("Eigenvalues:", eigenvalues)
                        print("Eigenvectors (columns):")
                        for vec in zip(*eigenvectors): 
                              # Transpose the eigenvector matrix
                            print([f"{x:.6f}" for x in vec])
                    case 12 :
                        mat1 = MatriceCalculator.get_matrix_input("Enter 1st Matrix :")
                        if mat1 is None :
                            break
                        mat2 = MatriceCalculator.get_matrix_input("Enter 2nd Matrix: ")
                        if mat2 is None :
                            break
                        result = mo.AugmentedMatrix(mat1,mat2)
                        if isinstance(result,list):
                            print("Augmentation  of 2 Matrices -> ")
                            MatriceCalculator.print_matrix(result)
                    case _:
                        print("Invalid Choice ! Try Again")
            case '3':
                x = int(input("1.Vector Addition(2-vectors)\n 2.Vector Scalar Multiplication \n 3.Vector Subtraction \n 4.Vector Dot product \n 5.Vector Magnitude \n 6.Angle between Vectors \n Enter your choice : "))
                vc = VectorCalculator()
                match x :
                    case 1 :
                        v1 = VectorCalculator.get_vector_input("First vector:")
                        if v1 is None: break
                        v2 = VectorCalculator.get_vector_input("Second vector:")
                        if v2 is None: break
                        result = vc.VectorAdd(v1,v2)
                        if isinstance(result, list):
                            VectorCalculator.print_vector(result)
                        else:
                            print(result)
                    case 2 :
                        v1 = VectorCalculator.get_vector_input("First vector:")
                        if v1 is None: break
                        v2 = VectorCalculator.get_vector_input("Second vector:")
                        if v2 is None: break
                        result = vc.VectorSub(v1,v2)
                        if isinstance(result, list):
                            VectorCalculator.print_vector(result)
                        else:
                            print(result)
                    case 3 :
                        v1 = VectorCalculator.get_vector_input("First vector:")
                        if v1 is None: break
                        v2 = VectorCalculator.get_vector_input("Second vector:")
                        if v2 is None: break
                        result = vc.VectorDotProduct(v1,v2)
                        print(f"Dot- Product :{result}")
                    case 4 :
                        v1 = VectorCalculator.get_vector_input("First vector:")
                        if v1 is None: break
                        scalar= float(input("Enter a Number"))
                        result = vc.Vector_scalarMul(v1,scalar)
                        if isinstance(result, list):
                            VectorCalculator.print_vector(result)
                        else:
                            print(result)
                    case 5 :
                        v1 = VectorCalculator.get_vector_input("Enter vector:")
                        if v1 is None: break
                        result = vc.VectorMagnitude(v1)
                        print(f"Magnitude: {result:.6f}")
                    case 6 :
                        v1 = VectorCalculator.get_vector_input("First vector:")
                        if v1 is None: break
                        v2 = VectorCalculator.get_vector_input("Second vector:")
                        if v2 is None: break
                        result = vc.AngleBetweenVectors(v1, v2)
                        print(f"Angle (radians): {result:.6f}")
                    case _:
                        print("Invalid input ! Try Again")
            case _:
                print("Invalid choice ! Try again")
    elif c == 5:
        print("Exiting calculator !Thanks for using it. ")
        break
    else :
        print("Invalid Choice ! PLEASE TRY AGAIN !")

         




                        





                    
                            

                        

                          

                            



                    
                






                






                    
        
   


                

    

    
                        


    
                    
                    


               
                    


                        

                              

                        



                        

                        
                    
                    

                        


                                



                            

                            

                                
                            






                        
                    
        
    
                    
                        






    


      


            
        


    
    





                   








                    



                    

                


        



                    


                    
                    


        
           
        





             

   
    

       

    
        

       
        
    
    





                






    





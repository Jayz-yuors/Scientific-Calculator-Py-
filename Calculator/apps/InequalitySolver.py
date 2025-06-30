import sympy as sp
class InequalitySolver:
    def solve_PolynomialInequality(self,coefficients,operator_type,variable_name):
        if not isinstance(coefficients,(list,tuple)):
            return f"Error : State the coefficients in list or tuple type"
        try :
            x = sp.symbols(variable_name)
            poly = sum( coeff * x ** i for i,coeff in enumerate(reversed(coefficients)))
            """
            coeffients = coeff, i = index.enumerate(interable)-> coefficients are reversed -> so
            [1,-3,2] will be [2,-3,1] with i = [0,1,2] respectively. then sum (...) ,at i = 0 
            it will be 2* x**0 that is 2 and so on constructing poly as x^2 -3x +2"""
            operator_list ={
                '>' :sp.Gt,
                '<' :sp.Lt,
                '>=':sp.Ge,
                '<=':sp.Le
            }
            if operator_type not in operator_list:
                return "Error:Invalid operator. Use '>', '<', '>=', or '<='"
            inequality = operator_list[operator_type](poly, 0)
            """
           operator_list[operator_type] retrieves the correct SymPy relational function (e.g., sp.Gt for '>').
           sp.Gt(poly, 0) then creates the inequality object: poly > 0."""
            solution = sp.solve_univariate_inequality(inequality, x, relational=False)
            #Relational = True -> provides the solution as a logical solution
             #Relational = False -> provides the solution as a Set of Intervals
            return solution
        except Exception as e :
            return f"Error : {str(e)}"
            
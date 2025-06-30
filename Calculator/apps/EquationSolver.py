import numpy as np 
import sympy as sp 
class EquationSolver:
    def solve_SimultaneousEquation(self,coefficients_matrix,constants_vector):
        if not isinstance(coefficients_matrix, (list, tuple)):
            return "Error: 'coefficients_matrix' must be a list of lists, tuple of tuples, or a NumPy array."
        if not isinstance(constants_vector, (list, tuple)):
            return "Error: 'constants_vector' must be a list, tuple, or a NumPy array."
        if not coefficients_matrix :
            return "Error :Provide Input for Matrix"
        if not constants_vector :
            return "Error:Provide Input for Vector"
        try:
            A = np.array(coefficients_matrix)
            b = np.array(constants_vector)
            if A.ndim != 2 :
                return f"Coefficient Matrix must be 2 - Dimensisonal "
            if b.ndim != 1 :
                return " Constant Vector must be 1 dimensional "
            if A.shape[0] != A.shape[1]:
                return "Error:Coefficient   Matric should be Squared "
            if A.shape[0] != len(b):
                return "Error : Matrix and Vector Dimensions mismatch:"
            solution = np.linalg.solve(A, b)
            return solution.tolist()
        except np.linalg.LinAlgError:
            return "Error: Singular matrix (no unique solution)"
        except Exception as e:
            return f"Error: {str(e)}"
    def solve_PolynomialEquation(self,coefficients):
        try :
            if not isinstance(coefficients,(list , tuple)):
                return f"Coefficients must be provided with in list or tuple type"
            if coefficients.ndim != 1:
                return "Error: Coefficients must represent a 1-dimensional sequence."
            if len(coefficients) < 2:
                return "Error: At least two coefficients are required for a polynomial of degree >= 1."
            if not coefficients: # Check if the list is empty
                return "Error: Coefficients list cannot be empty."
            for c in coefficients :
                if not isinstance(c,(int,float)):
                    return f"Error:All individual Coefficients must be int or float type"
            coeffs = [float(c) for c in coefficients]
            roots = np.roots(coeffs) #takes the coefficients of the PlyEq,solve it(companion matrix->EIGEN Values) and returns a list
            return [ complex(root) for root in roots ]
        except Exception as e :
            return f"Error:{str(e)}"
    def solve_SingleVariableEquation(self,equation_string,variable_name,initial_guess):
        try :
            x = sp.symbols(variable_name)
            equation = sp.sympify(equation_string)
            solution = sp.nsolve(equation,variable_name,initial_guess)
            return float(solution)
        except Exception as e :
            return f"Error :{str(e)}"
    


    
        
    
    

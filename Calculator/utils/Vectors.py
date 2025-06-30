import math
import numpy as np 
class VectorCalculator :
    def VectorAdd(self,v1,v2):
        try :
            nv1 = np.array(v1)
            nv2 = np.array(v2)
            if nv1.shape != nv2.shape :
                raise ValueError("Vectors should have the same shape for vector addtion")
            result = nv1 + nv2
            return result.tolist()
        except Exception as e :
            return f"An error occured while adding Vectors :{e}"
    def Vector_scalarMul(self,v1,scalar):
        try :
            nv1 = np.array(v1)
            if not isinstance(scalar,(int ,float)):
                raise ValueError("Scalar should be float or interger type :")
            result = nv1 * scalar
            return result.tolist()
        except Exception as e :
            return f"An error occured while multiplying Vector with scalar :{e}"
    def VectorSub(self,a,b):
        try :
            na = np.array(a)
            nb = np.array(b)
            if na.shape != nb.shape :
                raise ValueError("Vectors should have the same shape for vector subtraction")
            result = na + nb
            return result.tolist()
        except Exception as e :
            return f"An error occured while subtracting Vectors :{e}"
    def VectorDotProduct(self,a,b):
        try :
            v1 = np.array(a)
            v2 = np.array(b)
            if v1.shape != v2.shape :
                raise ValueError("Vectors should have the same shape for dot product")
            if v1.ndim !=1 or v2.ndim != 1:
                raise ValueError("Vectors should be one dimentional for dot product")
            result = np.dot(v1,v2)
            result = float(result)
            return result
        except Exception as e :
            return f"An error occured while doing dot product calculation :{e}"
    def VectorMagnitude(self,v):
        try :
            v = np.array(v)
            mag = np.linalg.norm(v)
            return float(mag)
        except Exception as e :
            return f"An error occured while calculating magnitude:{e}"
    def AngleBetweenVectors(slef,v1,v2):
        try :
            nv1 = np.array(v1)
            nv2 = np.array(v2)
            if nv1.shape != nv2.shape :
                raise ValueError("Vectors should have the same shape for vector angle calculation")
            if nv1.ndim != 1 or nv2.ndim != 1:
                raise ValueError("Vectors should be one dimensional for angle calculation")
            dot_product = np.dot(nv1, nv2)
            mag1 = np.linalg.norm(nv1)
            mag2 = np.linalg.norm(nv2)
            if mag1 == 0 or mag2 == 0:
                raise ValueError("Cannot calculate angle with zero magnitude vector")
            cos_theta = dot_product / (mag1 * mag2)
            cos_theta = np.clip(cos_theta, -1.0, 1.0)#clips value of costheta upto a range
            angle = math.acos(cos_theta)
            return float(angle)
        except Exception as e :
            return f"An error occured while calculating angle between the vectors"
    @staticmethod
    def get_vector_input(prompt):
        print(prompt)
        n = int(input("Enter number of elements in the vector"))
        elements = input(f"Enter {n} elements seperated by spaces :").split()
        if len(elements) !=n:
            print(f"Error: Expected {n} elements, got {len(elements)}")
            return None
        try:
            return [float(x) for x in elements]
        except ValueError:
            print("Error: All elements must be numbers")
            return None
    @staticmethod
    def print_vector(v):
        print("Vector:", " ".join(f"{elem:.4f}" for elem in v))

        
        

            




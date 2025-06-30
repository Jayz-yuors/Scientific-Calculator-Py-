import numpy as np
class MatriceCalculator :
    def MatriceAdd(self,mat1,mat2):
        try :
            nmat1 = np.array(mat1)
            nmat2 = np.array(mat2)
            if nmat1.shape != nmat2.shape :
                raise ValueError("Matrices should have the same dimensions for Addition purpose")
            result = nmat1 + nmat2
            return result.tolist()
        except Exception as e :
            return f"An error occured while adding matrices:{e}"
    def MatriceAdd_3(self,mat1,mat2,mat3):
        try :
             nmat1 = np.array(mat1)
             nmat2 = np.array(mat2)
             nmat3 = np.array(mat3)
             if not (nmat1.shape == nmat2.shape == nmat3.shape) :
                 raise ValueError("Matrices should have the same dimensions for addtiion ")
             result = nmat1 + nmat2 + nmat3
             return result.tolist()
        except Exception as e :
             return f"An error occured while adding matrices:{e}"
    def MatriceSub(self,mat1,mat2):
        try :
            a = np.array(mat1)
            b = np.array(mat2)
            if a.shape != b.shape :
                raise ValueError(" Matrices should have the same dimensions for Subtraction ")
            result = a - b
            return result.tolist()
        except Exception as e :
             return f"An error occured while subtracting matrices:{e}"
    def MatricesMul(self,mat1,mat2):
        try :
            a =np.array(mat1)
            b = np.array(mat2)
            if a.shape[1] != b.shape[0] :
                raise ValueError(" No of rows of first Matrix should be equal to No of columns of second Matrix for Multiplication ")
            result = np.dot(a,b)
            return result.tolist()
        except Exception as e:
             return f"An error occured while Multiplicating matrices:{e}"
    def Matrice_scalarMul(self,mat1,scalar):
        try :
            a= np.array(mat1)
            if not isinstance(scalar,(int,float)):
                raise ValueError("Scalar should be an interger or float")
            result = a * scalar
            return result.tolist()
        except Exception as e :
            return f"An error occured while Multiplicating matrice with scalar:{e}"
    def MatriceDeterminant(self,mat1):
        try :
            a = np.array(mat1)
            if a.shape[0] != a.shape[1]:
                raise ValueError("Matrix should be sqared for Determninant:")
            result = np.linalg.det(a)
            return result 
        except Exception as e :
             return f"An error occured while finding Determinant:{e}"
    def MatriceInverse(self,mat1):
        try :
            a = np.array(mat1)
            if a.shape[0] != a.shape[1]:
                raise ValueError("Matrix should be sqared for Determninant:")
            if np.linalg.det(a) == 0 :
                raise ValueError("Matrix is singular and cannot be inverted")
            inverse = np.linalg.inv(a)
            return inverse.tolist()
        except Exception as e :
            return f"An error occured while finding incerse of the Matrice:{e}"
    def MatriceTranspose(self,mat1) :
        try :
            a = np.array(mat1)
            result = np.transpose(a)
            return result.tolist()
        except Exception as e :
             return f"An error occured while Transposing Matrice :{e}"
    def MatriceRank(self,mat1):
        try :
            a =  np.array(mat1)
            result = np.linalg.matrix_rank(a)
            return result
        except Exception as e :
            return f"An error occured while finding Rank of the Matrix:{e}"
    def MatriceEigenValues(self,mat1):
        try :
            a = np.array(mat1)
            if a.shape[0] != a.shape[1]:
                raise ValueError("Matrix should be squared for Eigen value calculation")
            e1 = np.linalg.eigvals(a)
            return e1.tolist()
        except np.linalg.LinAlgError as e:
            print(f"Linear algebra error during Eigenvalue calculation: {e}")
        except Exception as e :
            return f"An error occured while finding Eigen Values of the Matirx:{e}"
    def MatriceEigenVectors(self,mat1):
        try :
            a = np.array(mat1)
            if a.shape[0] != a.shape[1]:
                raise ValueError("Matrix should be squared for EigenVector calculation")
            eigenvalues,eigenvectors = np.linalg.eig(a)
            return eigenvalues.tolist(),eigenvectors.tolist()
        except np.linalg.LinAlgError as e:
            return f"Linear  algebra error during Eigenvalue calculation: {e}"
        except Exception as e :
            return f"An error occured while finding Eigen Vectors of the Matirx:{e}"
    def AugmentedMatrix(self,mat1,mat2):
        try :
            nmat1 = np.array(mat1)
            nmat2 = np.array(mat2)
            if nmat1.shape[0] != nmat2.shape[0] :
                raise ValueError(" AUGMENTATION requires Matrices of same rows")
            result = np.hstack((nmat1,nmat2))
            return result.tolist()
        except Exception as e :
            return f"An error occured while Augmenting Matrice :{e}"
    @staticmethod
    def get_matrix_input(prompt):
        print(prompt)
        rows = int(input("Enter no of rows :"))
        cols = int(input("Enter number of columns"))
        matrix = []
        for i in range (rows):
            row_input = input(f"Enter row {i + 1} elements seperated by one space : ")
            row = [float(x) for x in row_input.strip().split()]
            if len(row) != cols:
                print(f"Error: You must enter exactly {cols} elements for this row ")
                return None
            matrix.append(row)
        return matrix
    @staticmethod
    def print_matrix(mat):
        print("Resultant Matrix:")
        for row in mat:
           print(" ".join(f"{elem:.2f}" for elem in row))

    
                


    
                




    

            
            

    

            

            
            

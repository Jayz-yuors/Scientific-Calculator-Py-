import sympy as sp
import numpy as np
class NumericalFunction :
    def Differentiation(self,eq1,var,val):
        try :
            if not isinstance(val ,(float,int)) :
                return f"Error:value should be float or integer type"
            dvar =sp.Symbol(var)
            seq1 = sp.simplify(eq1)
            result = sp.diff(seq1,dvar) # differentaite wrt to var
            ans = result.subs(dvar,val).evalf() # evaluation of the result expression
            ans = float(ans)
            return result , ans 
        except sp.SimpifyError:
            return f"Error:Invalid expression or variable format"
        except TypeError as e :
            return f"Error:Invalid input type : {e}"
        except Exception as e:
            return f"An unexpected error occurred during differentiation: {e}"
    def Integration (self,eq1,var,val):
        try:
             if not isinstance(val ,(float,int)) :
                return f"Error:value should be float or integer type"
             ivar = sp.Symbol(var)
             seq1 = sp.simplify(eq1)
             result = sp.integrate (seq1,ivar)
             ans = result.subs(ivar,val).evalf()
             ans = float(ans)
             return result,ans
        except sp.SympifyError:
            return f"Error: Invalid expression or variable format", None
        except TypeError as e:
            return f"Error: Invalid input type: {e}", None
        except Exception as e:
            return f"An unexpected error occurred during integration: {e}", None
        

             
            
    


        
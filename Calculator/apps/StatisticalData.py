import math
import numpy as np
class StatisticalData:
    def one_vardata(self,data:list):
        try :
            if not data or not isinstance(data,(list)):
                return f"Error:Input should be a non-empty list of numbers:"
            data = [float(x) for x in data]
            return data
        except Exception as e :
            return f"Error processing Data:{e}"
    def get_mean(self,data):
        return np.mean(data)
    def get_sum(self,data):
        return np.sum(data)
    def get_sum_squared(self,data):
        return np.sum(np.square(data))
    def get_stdev_population(self,data):
        return np.std(data,ddof = 0)#ddof -> delta degree of Freedom,formula
    def get_stdev_sample(self,data):
        return np.std(data,ddof = 1)
    def get_count(self,data):
        return len(data)
    def get_min(self,data):#smallest value
        return np.min(data)
    def get_max(self,data):#biggest value
        return np.max(data)
    def get_median(self,data):
        return np.median(data)
    def get_quartiles (self,data):
        q1 = np.percentile(data,25) # term = n+1/4
        q2 = np.percentile(data,50)  # term = n+1/2
        q3 = np.percentile(data,75)   # term = 3 *(n+1)/4
        return (q1,q2,q3)
    def all_functions(self,data):
        a = self.one_vardata(data)
        if isinstance(a,str):
            return a
        b = self.get_mean(a)
        c = self.get_sum(a)
        d = self.get_sum_squared(a)
        e = self.get_stdev_population(a)
        f = self.get_stdev_sample(a)
        g = self.get_max(a)
        h = self.get_count(a)
        i =self.get_min(a)
        j = self.get_median(a)
        k = self.get_quartiles(a)
        return f"Data :{a}\n Mean:{b}\n Sum :{c}\nSquared Sum :{d} \n STDEV POPULATION(ddof = 0):{e} \n STDEV SAMPLE(ddof = 1):{f} \n MAX among Data :{g} \n Length of Data :{h} \n MIN among Data :{i} \n MEDIAN of Data : {j} \n Quartiles of Data(25-50-75 respectively):{k} \n "
    def two_vardata(self,xdata:list,ydata:list):
        try :
            if not xdata or not ydata or not isinstance(xdata, list) or not isinstance(ydata, list):
                 return "Error: Input should be two non-empty lists of numbers."
            xdata = [float(x) for x in xdata]
            ydata = [float(y) for y in ydata]
            if len(xdata) != len(ydata):
                 return "Error: Both lists must have the same length."
            return xdata, ydata
        except Exception as e:
            return f" Error Processing Data"
    def get_mean_x(self,xdata):
        return np.mean(xdata)
    def get_mean_y(self,ydata):
        return np.mean(ydata)
    def get_sum_x(self,xdata):
        return np.sum(xdata)
    def get_sum_y(self,ydata):
        return np.sum(ydata)
    def _get_sum_x_squared(self, x_data):
        return np.sum(np.square(x_data))
    def _get_sum_y_squared(self, y_data):
        return np.sum(np.square(y_data))
    def _get_stdev_population_x(self, x_data):
        return np.std(x_data, ddof=0)
    def _get_stdev_sample_x(self, x_data):
        return np.std(x_data, ddof=1)
    def _get_stdev_population_y(self, y_data):
        return np.std(y_data, ddof=0)
    def _get_stdev_sample_y(self, y_data):
        return np.std(y_data, ddof=1)
    def get_sum_xy(self,xdata,ydata):
        return np.sum(np.array(xdata) *np.array(ydata))
    def perform_linear_regression(self, x_data, y_data):
        # regression line -> y = a + bx
        x = np.array(x_data)
        y = np.array(y_data)
        n = len(x)
        if n != len(y):
            return "Error: x_data and y_data must have the same length."
        if n < 2:
            return "Error: At least two data points are required."
        mean_x = np.mean(x)
        mean_y = np.mean(y)
        SS_xy = np.sum((x - mean_x) * (y - mean_y))
        SS_xx = np.sum((x - mean_x) ** 2)
        b = SS_xy / SS_xx
        a = mean_y - b * mean_x
        # Pearson correlation coefficient
        r = np.corrcoef(x, y)[0, 1]
        return f"a:{a}\n b:{b}\n r:{r}"
    def perform_quadratic_regression(self, x_data, y_data):
        x = np.array(x_data)
        y = np.array(y_data)
        if len(x) != len(y):
            return "Error: x_data and y_data must have the same length."
        if len(x) < 3:
            return "Error: At least three data points are required for quadratic regression."
        # Fit a quadratic: y = c2*x^2 + c1*x + c0
        coeffs = np.polyfit(x, y, 2)
        # Return in the form y = a + bx + cx^2
        c, b, a = coeffs
        return f"a:{a}\n b:{b}\n c:{c}"

    

    
    
    
    
           
        
        
             
           
             
                 






    

    
    

        

             

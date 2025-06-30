import numpy as np
from scipy.stats import norm,binom,poisson
class DistributionData:
    def normal_pdf(self,x,mean,stdev):
        if not all(isinstance(val,(int,float))for val in [x,mean,stdev]):
            raise TypeError("Error:x, mean, and std_dev must be int or float")
        return norm.pdf(x,loc=mean,scale= stdev)
    def normal_cdf(self,x,mean,stdev):
        if not all(isinstance(val,(int,float))for val in [x,mean,stdev]):
            raise TypeError("Error:x, mean, and std_dev must be int or float")
        return norm.cdf(x,loc=mean,scale=stdev)
    def inverse_normal_cdf(self, probability, mean, std_dev):
        if not all(isinstance(val, (int, float)) for val in [probability, mean, std_dev]):
            raise TypeError("Error:probability, mean, and std_dev must be int or float")
        return norm.ppf(probability, loc=mean, scale=std_dev)
    def binomial_pdf(self,k,n,p):
        if not all(isinstance(val,(float,int)) for val in [k,n,p]):
            raise TypeError("Error:k,n,p must be int or float")
        return binom.pmf(k,n,p)
    def binomial_cdf(self,k,n,p):
        if not all(isinstance(val,(float,int)) for val in [k,n,p]):
            raise TypeError("Error:k,n,p must be int or float")
        return binom.cdf(k,n,p)
    def poisson_pdf(self, k, lambda_val):
        if not all(isinstance(val, (int, float)) for val in [k, lambda_val]):
            raise TypeError("Error:k and lambda_val must be int or float")
        return poisson.pmf(k, lambda_val)
    def poisson_cdf(self, k, lambda_val):
        if not all(isinstance(val, (int, float)) for val in [k, lambda_val]):
            raise TypeError("Error:k and lambda_val must be int or float")
        return poisson.cdf(k, lambda_val)
    
    
    

    
    

        
